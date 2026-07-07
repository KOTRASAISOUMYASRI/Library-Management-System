# Library Management System

## Overview

The Library Management System is a console-based application developed using Python and MySQL to automate basic library operations. It enables users to manage book records, issue and return books, update book details, and visualize library data through a simple menu-driven interface.

This project was developed as part of my undergraduate coursework to demonstrate database connectivity and CRUD operations using Python.

---

## Learning Outcomes

This project helped me gain practical experience with:

- Python programming
- MySQL database connectivity using PyMySQL
- CRUD operations
- Menu-driven application development
- Data visualization using Matplotlib

## Features

- Add new books to the library database
- Display all available books
- Issue books to users
- Record returned books
- Update existing book details
- Delete book records
- Visualize book availability using a bar graph

---

## Technologies Used

- Python
- MySQL
- PyMySQL
- Matplotlib

---

## Project Structure

```
Library-Management-System/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── src/
│   └── main.py
│
├── database/
│   └── library_management.sql
│
└── screenshots/
    ├── home.png
    ├── add_book.png
    ├── issue_book.png
    ├── display_books.png
    ├── submit_book.png
    ├── update_book.png
    ├── delete_book.png
    └── graph.png
```

---

## Installation

1. Clone the repository.

```bash
git clone https://github.com/KOTRASAISOUMYASRI/Library-Management-System.git
```

2. Navigate to the project directory.

```bash
cd Library-Management-System
```

3. Install the required Python packages.

```bash
pip install -r requirements.txt
```

4. Create the database by executing the SQL script located in the `database` folder.

5. Open `src/main.py` and update the MySQL connection details with your username and password.

6. Run the application.

```bash
python src/main.py
```

---

## Database

Run the SQL script below to create the required database and tables.

```
database/library_management.sql
```

---

## Screenshots

### Home Screen

![Home](screenshots/home.png)

### Add Book

![Add Book](screenshots/add_book.png)

### Display Books

![Display Books](screenshots/display_books.png)

### Issue Book

![Issue Book](screenshots/issue_book.png)

### Return Book

![Return Book](screenshots/submit_book.png)

### Update Book

![Update Book](screenshots/update_book.png)

### Delete Book

![Delete Book](screenshots/delete_book.png)

### Book Statistics

![Graph](screenshots/graph.png)

---

## Future Enhancements

- Develop a graphical user interface (GUI)
- Implement user authentication
- Add search and filtering options
- Generate reports for issued and returned books
- Export reports in PDF or Excel format

---

## Author

**Kotra Sai Soumya Sri**

B.Tech in Computer Science and Engineering  
PES University
