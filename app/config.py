import os
from dotenv import load_dotenv

# it loads variables from a .env file into environment variables
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # to disable a warning message