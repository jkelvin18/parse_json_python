import sqlite3
from helpers.utils import (
    read_json_file,
    create_tables,
    insert_data_into_tables,
)


def main():
    """
    Main function to execute the script.

    This function reads data from a JSON file, connects to a SQLite database,
    creates tables in the database, inserts the data into the tables, and commits
    the changes. It handles errors that may occur during these processes.
    """

    # Define file paths
    json_file_path = (
        "C:/Users/win/Documents/personal projects/create_json/users_hard.json"
    )
    db_file_path = "C:/db_prd/db_prd.db"

    # Read data from JSON file
    data = read_json_file(json_file_path)

    # Connect to the SQLite database
    with sqlite3.connect(db_file_path) as conn:
        # Create a cursor
        c = conn.cursor()

        # DROP TABLE
        c.execute("DROP TABLE IF EXISTS users")
        c.execute("DROP TABLE IF EXISTS addresses")
        c.execute("DROP TABLE IF EXISTS skills")

        # Create tables
        create_tables(c)

        # Insert data into tables
        insert_data_into_tables(c, data)

        # Commit our command
        conn.commit()


# The statement "if name == 'main': main()" ensures that the main function is only run when this script is directly executed,
# and not when the module is imported into other scripts.
# This allows the module's functions to be reused elsewhere without running the entire script.
if __name__ == "__main__":
    main()
