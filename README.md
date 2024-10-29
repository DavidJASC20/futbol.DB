FIFA Soccer Database and Web Interface:

A Python, SQLAlchemy, and Flask project for managing and querying FIFA soccer data, including player, club, and competition information.

About:

This project creates a database backend and web interface to manage and query soccer records. The database parses JSON files with player, club, and competition details. Users can add favorite players and clubs through the interface, updating the SQLAlchemy database on the backend.

Installation:

Clone the repository:
git clone https://github.com/username/futbol.DB.git

Set up a virtual environment:

python -m venv venv
cd venv
source Scripts/activate  # `source bin/activate` on macOS/Linux

Install dependencies:

pip install flask flask-wtf SQLAlchemy

Import SQLAlchemy in your Python environment:

import sqlalchemy

Usage
To use this project:

Run Project_load.py to initialize and load the database.
Run Project_routes.py, which creates a web link for easy access (Ctrl+Click the link in your console to open).
Use Project_query.py to run queries on the database tables, with output returned to the console.

Technologies:
Python - Programming language
SQLAlchemy - ORM
Flask - Web framework
