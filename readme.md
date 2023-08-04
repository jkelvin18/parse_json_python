# SQLite User Data Importer

This Python script populates an SQLite database with user data from a JSON file. It's ideal for setting up mock data for testing or demonstrations.

## Overview

The script reads a JSON file, where each object represents a user and their associated data. The user information is stored in the 'users' table, address in the 'addresses' table, and skills in the 'skills' table.

## Database Structure

The SQLite database consists of three tables:

- `users`: Stores user information, including name, email, and date of birth.
- `addresses`: Stores user's address information, including street, city, state, and country.
- `skills`: Stores user's skills.

Each table includes a foreign key `user_id` that connects the user's information, address, and skills.

## Installation

To run the script, you'll need to have Python 3 installed on your machine.

1. Clone this repository to your machine:

bash
git clone https://github.com/jkelvin18/parse_json_python.git

2. Navigate to the project directory:

bash
cd your-repository

3. pip install -r requirements.txt

## Usage
To populate your SQLite database with user data, you'll need to provide a JSON file with the appropriate structure.

An example of the JSON data structure:

[
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "dob": "2000-01-01",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "country": "Country"
        },
        "skills": ["Python", "SQL"]
    }
]

Run the script and pass the path to your JSON file as an argument:

python main.py /path/to/your/data.json

The script will populate your SQLite database with the data from the JSON file.

## Tests
This repository also contains tests to verify the functionality of the code.

To run the tests, use the following command:

pytest tests/

Feel free to copy this markdown code and adjust it to your needs!
