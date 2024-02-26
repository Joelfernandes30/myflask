from sqlalchemy import create_engine, text
import pymysql



user = 'sql6686805'
password = 'QbB1rbbFeL'
host = 'sql6.freesqldatabase.com'
port = 3306
database = 'sql6686805'


def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )

engine = get_connection()

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(dict(row._mapping))

    print(result_dicts)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs






