import sqlite3

#  sqlite database setup
connection=sqlite3.connect("student.db")
db=connection.cursor()

# Create the table
create_table_query="""
CREATE TABLE STUDENTS (
    NAME VARCHAR(100),
    SECTION VARCHAR(10),
    ROLL_NUMBER INT PRIMARY KEY,
    MARKS DECIMAL(5, 2),
    MAJOR VARCHAR(50),
    MINOR VARCHAR(50)
);
"""
db.execute(create_table_query)

# Inserting records into STUDENT table
sql_query = """INSERT INTO STUDENTS (NAME, SECTION, ROLL_NUMBER, MARKS, MAJOR, MINOR) VALUES (?, ?, ?, ?, ?, ?)"""
values = [
('John Doe', 'A', 101, 85.5, 'Computer Science', 'Mathematics'),
('Jane Smith', 'B', 102, 92.0, 'Electrical Engineering', 'Physics'),
('Emily Johnson', 'A', 103, 78.5, 'Mechanical Engineering', 'Chemistry'),
('Michael Brown', 'C', 104, 88.0, 'Biology', 'Environmental Science'),
('Alice White', 'B', 105, 91.0, 'Computer Science', 'Physics'),
('David Green', 'C', 106, 84.5, 'Computer Science', 'Psychology'),
('Sophia Davis', 'D', 107, 79.0, 'Chemistry', 'Biology'),
('Liam Miller', 'A', 108, 93.5, 'Mechanical Engineering', 'Mathematics'),
('Olivia Harris', 'B', 109, 95.0, 'Biology', 'Geography'),
('Ethan Clark', 'C', 110, 82.5, 'Physics', 'Computer Science')
]

db.executemany(sql_query, values)
connection.commit()

# Display the records
data=db.execute("""Select * from STUDENTS""")

for row in data:
    print(row)

if connection:
    connection.close()