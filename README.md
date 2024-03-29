# Library-management-system


This is a simple library management system that allows users to borrow and return books. It is built using Python and Flask, and it uses a SQLite database.

## Features

* Users can register and log in to the system.
* Users can browse a list of books.
* Users can search for books by title or author.
* Users can borrow books.
* Users can view a list of their borrowed books.
* Users can return books.

## Requirements

* Python 3.6 or higher
* Flask 2.2.5 or higher
* SQLite 

## Installation

1. Clone the repository from GitHub:

```bash
git clone https://github.com/satyajit-2003/Library-management-system.git
```

2. Create a virtual environment and activate it.

```bash
python -m venv venv && source venv/bin/activate
```

3. Install the dependencies.
```bash
pip install -r requirements.txt
```
4. Create a file `main.db` in databases folder, execute the `create_query.sql` file in the same folder to create the tables and `books.sql` to populate the books table.
5. Run the application by executing `python main.py`.

## Usage

The application is now running on your local machine. You can access it at http://localhost:8000.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request.

## Bugs

If you find a bug, please open an issue on the GitHub repository.

## License

The project is licensed under the MIT License.
