# importing libraries
import os
import sqlite3
import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# loading groq-api-key stored in .env file
load_dotenv()

# fine tuning the LLM to give SQL query
def get_sql_query(user_query):
    groq_sys_prompt = ChatPromptTemplate.from_template("""
        You are an expert in converting English questions to SQL queries!
        The SQL database has the name STUDENTS and has the following columns - NAME, SECTION, 
        ROLL_NUMBER, MARKS, MAJOR and MINOR. For example, 
        Example 1 - How many students are registered?, 
                    the SQL command will be something like this SELECT COUNT(*) FROM STUDENTS;
        Example 2 - Tell me all the students studying Computer Science COURSE?, 
                    the SQL command will be something like this SELECT * FROM STUDENTS 
                    where COURSE="Computer Science"; 
        also the sql code should not have ``` in beginning or end and sql word in output.
        Now convert the following question in English to a valid SQL Query: {user_query}. 
        No preamble, only valid SQL please
        """)
    
    model="llama3-8b-8192"
    llm = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    model_name=model
    )

    chain = groq_sys_prompt | llm | StrOutputParser()
    response = chain.invoke({"user_query": user_query})
    return response

# querying the database
def return_sql_response(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()


# streamlit interface along with inline html
def main():
    st.set_page_config(page_title="Text To SQL", layout = "wide")
    st.markdown(
        "<h1 style='text-align: center; color: #FF5733;'>Talk to your Database!</h1>", 
        unsafe_allow_html=True
    )
    st.markdown("""
    <p style="text-align: center;">Enter a natural language query to interact with your SQL database. 
    For example, you can ask questions like <b>'What is the total number of students in the database?'</b> 
    or <b>'Show me all students with more than 80 marks.'</b> or <b>'List all the majors that students are enrolled in.' </b>
    Your query doesn’t need to be grammatically perfect, as long as the requirement is clear😀.</p>
    """, unsafe_allow_html=True)

    user_query = st.text_input("Input your query:", placeholder="Type your query here...")
    submit = st.button("Submit", use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if submit:
        sql_query = get_sql_query(user_query)
        retrieved_data = return_sql_response(sql_query)
        
        st.markdown(f"### SQL Query: `{sql_query}`", unsafe_allow_html=True)
        st.subheader("Result:")
        
        if retrieved_data:
            for row in retrieved_data:
                formatted_row = ' | '.join(str(item) for item in row)
                st.markdown(f"**{formatted_row}**", unsafe_allow_html=True)
        else:
            st.write("No results found for this query.")
    st.markdown("""
    <footer style="text-align: center; color: #888; font-size: 12px;">
    <p>Powered by <a href="https://streamlit.io" target="_blank">Streamlit</a></p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()