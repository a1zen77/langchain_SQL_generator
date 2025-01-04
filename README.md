# Natural Language Database Interaction Application

This is an application that enables interaction with databases through natural language. It simplifies the process of querying databases for non-technical users, allowing them to retrieve data using simple English.

## Features

- **Natural Language Queries**: Users can query the database using plain English (e.g., "What is the total sales for 2024?" or "List all students in the Physics department").
  
- **Query Interpretation**: The application uses a fine-tuned GROQ model to convert the natural language input into SQL queries.

- **Database Compatibility**: Works with sqlite databases (eg., student.db)

- **Fine-Tuning**: Used prompt engineering to ensure that to LLM only responds with SQL query, nothing else.

- **Inter-Face**: Developed a Streamlit interface for user input and seamless interaction with the sqlite database.


<img width="1388" alt="Screenshot 2025-01-04 at 4 33 40 PM" src="https://github.com/user-attachments/assets/374bdf84-9934-4b08-b2f3-f43aaaaef144" />
