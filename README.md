
# 📰 Articles — Without SQLAlchemy

## 📚 About This Project

This project is part of a **Phase 3 Object-Relational Mapping (ORM)** lab. It is designed for learners who are exploring how to:

- Connect Python code to a **SQLite3** database,
- Use **raw SQL queries** instead of ORM libraries like SQLAlchemy,
- Build classes and use **Object-Oriented Programming (OOP)** principles, and
- Model relationships between real-world entities (authors, magazines, and articles).

You’ll learn how to interact with a database using pure Python — no shortcuts, just fundamentals!

---

## 🧠 Learning Goals

By working through this project, you’ll practice:

- Structuring a Python project with reusable components,
- Writing raw SQL commands in `.sql` and Python,
- Managing class instances and relationships (e.g. an Author has many Articles),
- Testing functionality using a scratch file (`scratchpad.py`).

---

## 🗂️ Project Structure

Articles---without-SQLAlchemy/
├── lib/
│ ├── db/
│ │ ├── connection.py # Handles DB connection setup
│ │ ├── seed.py # Populates the database with test data
│ │ └── schema.sql # SQL file to create tables
│ ├── models/
│ │ ├── author.py # Author class
│ │ ├── article.py # Article class
│ │ └── magazine.py # Magazine class
├── scripts/
│ └── setup_db.py # Script to create tables from schema.sql
├── scratchpad.py # Used for testing your models
├── Pipfile / Pipfile.lock # For dependency management via pipenv


