from flask_sqlalchemy import SQLAlchemy
import os

# Load database configuration from environment variables
def get_db_uri():
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT', '3306')
    db_name = os.getenv('DB_NAME')
    
    DB_URI = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    return DB_URI

db = SQLAlchemy()