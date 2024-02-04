from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DB = os.getenv("DB_DB")

engine = create_engine('mysql+pymysql://DB_USERNAME:DB_PASSWORD@DB_HOST/DB_DB')