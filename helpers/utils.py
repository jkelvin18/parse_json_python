import json
import os


def read_json_file(file_path):
    """
    Read and return data from a JSON file.

    This function loads JSON from the provided file path. It raises a
    FileNotFoundError if the file does not exist.

    Parameters:
    file_path (str): The location of the file to read.

    Returns:
    dict: A dictionary representation of the JSON data.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data


# Data split into four tables (users, addresses, skills and projects ) to model
# 'one-to-many' relationship between users/skills and users/projects.
# This facilitates queries and data maintenance."
# create tables
def create_tables(cursor):
    """
    Create 'users', 'addresses', and 'skills' tables.

    This function executes SQL commands to create 'users', 'addresses', and
    'skills' tables if they do not already exist in the database.

    Parameters:
    cursor (sqlite3.Cursor): A SQLite cursor.
    """

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            dob TEXT
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            street TEXT,
            city TEXT,
            state TEXT,
            country TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            skill TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """
    )


def insert_data_into_tables(cursor, data):
    """
    Insert data into 'users', 'addresses', and 'skills' tables.

    This function iterates over the user data and inserts the data into the
    'users', 'addresses', and 'skills' tables in the database.

    Parameters:
    cursor (sqlite3.Cursor): A SQLite cursor.
    data (dict): The user data to insert into the tables.
    """

    for user in data:
        cursor.execute(
            "INSERT INTO users (name, email, dob) VALUES (?, ?, ?)",
            (user["name"], user["email"], user["dob"]),
        )
        user_id = cursor.lastrowid

        address = user["address"]
        cursor.execute(
            "INSERT INTO addresses (user_id, street, city, state, country) VALUES (?, ?, ?, ?, ?)",
            (
                user_id,
                address["street"],
                address["city"],
                address["state"],
                address["country"],
            ),
        )

        for skill in user["skills"]:
            cursor.execute(
                "INSERT INTO skills (user_id, skill) VALUES (?, ?)",
                (user_id, skill),
            )
