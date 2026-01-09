# ⚽ FIFA Soccer Database & Web Interface

A backend-focused project built with **Python**, **SQLAlchemy**, and **Flask** for managing and querying FIFA soccer data, including players, clubs, and competitions.

---

## 📌 Overview

This project implements a relational database and web interface to manage FIFA soccer records.  
Structured JSON files are parsed and persisted using SQLAlchemy, allowing users to query data and manage favorite players and clubs through a Flask-based interface.

---

## 📊 Features

- Parses structured JSON data containing player, club, and competition information
- Implements a relational database using SQLAlchemy ORM
- Provides Flask routes for viewing and managing soccer records
- Allows users to add favorite players and clubs, persisting selections to the database
- Supports console-based querying for backend data analysis

---

## 🧠 Tech Stack

- **Python**
- **Flask** – Web framework
- **SQLAlchemy** – ORM and database modeling
- **SQLite** – Local relational database
- **JSON** – Data source format

---

## 📂 Project Structure

- `Project_load.py` – Initializes the database and loads JSON data into tables
- `Project_routes.py` – Defines Flask routes and launches the web interface
- `Project_query.py` – Executes database queries and outputs results to the console

---

## ▶️ Installation & Setup

```bash
1. Clone the repository:

git clone https://github.com/DavidJASC20/futbol.DB.git

2. Create and activate a virtual environment:

python -m venv venv
source venv/Scripts/activate   # Windows
# source venv/bin/activate     # macOS/Linux

3. Install dependencies:

pip install flask flask-wtf SQLAlchemy

▶️ Running the Project

1. Initialize and load the database:
python Project_load.py

2. Launch the Flask web interface:
python Project_routes.py

3. Run database queries:
python Project_query.py
