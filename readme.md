# Flask MySQL Application

Simple Flask application that connects to a MySQL database using SQLAlchemy and `pymysql`.
The application includes a `Recipe` model and basic CRUD operations.

## Features

- Flask web framework
- SQLAlchemy ORM
- MySQL database connection using `pymysql`
- Environment variable configuration for database credentials
- Logging configuration
- Modular project structure for maintainability

## Requirements

- Python 3.x
- MySQL server
- Virtual environment (recommended)

## Installation

1. **Create and activate a virtual environment**

   - On macOS and Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**

   Create a `.env` file (or rename/clone from `env.example`) in the root directory and add the following:

   ```plaintext
   DB_USERNAME=your_username
   DB_PASSWORD=your_password
   DB_HOST=your_host
   DB_NAME=your_database
   DB_PORT=your_database_port
   ```

4. **Run the application**
   ```bash
   flask run
   ```

## Project Structure

1. **Models**

   `modules/common/db.py`: Initializes the SQLAlchemy connection string, instance.

   `modules/recipe/models.py`: Defines the Recipe model.

2. **Routes**

   `modules/recipe/routes.py`: Defines the routes for the Recipe api.
