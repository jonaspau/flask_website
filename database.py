from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_DB = os.getenv("DB_DB")

db_connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DB}'

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ca": "/etc/ssl/certs/ca-certificates.crt"
                           }
                       }
                       )


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

    jobs = []
    # reads through the sglalchemy output and returns a dictionary with each job as a row
    for row in result.all():
        jobs.append(dict(row._mapping))

    return jobs