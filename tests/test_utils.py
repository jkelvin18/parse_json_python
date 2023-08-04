from unittest.mock import MagicMock
import pytest
import os
import json
import sqlite3
from helpers.utils import (
    read_json_file,
    create_tables,
    insert_data_into_tables,
)

# Example mock data
user_data = [
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "dob": "2000-01-01",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "country": "Country",
        },
        "skills": ["Python", "SQL"],
    }
]


# Testing the read_json_file function
def test_read_json_file():
    with pytest.raises(FileNotFoundError):
        read_json_file("non_existent_file.json")


# Testing the create_tables function
def test_create_tables():
    mock_cursor = MagicMock()

    create_tables(mock_cursor)

    # the number of calls to execute should be 3 for creating 3 tables
    assert mock_cursor.execute.call_count == 3


# Testing the insert_data_into_tables function
def test_insert_data_into_tables():
    mock_cursor = MagicMock()

    insert_data_into_tables(mock_cursor, user_data)

    # the number of calls depends on the number of users and their skills
    assert mock_cursor.execute.call_count == 4
