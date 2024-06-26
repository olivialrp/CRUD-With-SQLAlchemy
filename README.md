﻿# CRUD-With-SQLAlchemy
 
# User Management System with Login

## Project Overview
This project is a user management system with a login page, using SQLAlchemy ORM for database interactions and Streamlit for the web interface. It includes CRUD operations for user records and authentication functionality.

## Installation
To run this project, you will need Python installed on your system. Additionally, you'll need to install the following packages:
- SQLAlchemy
- Werkzeug
- Streamlit

You can install these with pip using the following command:
pip install sqlalchemy werkzeug streamlit

## Database Setup
The script automatically creates a SQLite database file `bd_users.sqlite` in the current directory if it doesn't exist.

## Usage
Run the Streamlit app using the command:
streamlit run login_page.py

The login page allows users to select their username from a dropdown and enter their password. Successful authentication will display a welcome message and set the session state to logged in.

## Security
Passwords are hashed using Werkzeug's `generate_password_hash` and verified with `check_password_hash`.

## More comments about Login Page
The login page is created using Streamlit's container feature, providing an isolated space for login functionality. It uses a select box for username selection and a text input for password entry. The `verifies_password` method checks the entered password against the hashed password in the database.
