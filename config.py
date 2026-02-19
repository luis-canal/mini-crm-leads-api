import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
DATABASE_NAME = os.getenv("DATABASE_NAME")
API_KEY = os.getenv("API_KEY")
ENV = os.getenv("ENV")

print("DATABASE_NAME:", DATABASE_NAME)
