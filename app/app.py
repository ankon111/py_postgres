import time
import random
import sqlalchemy as sql
from sqlalchemy import create_engine

db_name = 'lotto'
db_user = 'postgres'
db_pass = 'postgres1234'
db_host = 'db'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
engine = create_engine(db_string)

def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    with engine.connect() as conn:
        conn.execute(sql.text(f"INSERT INTO numbers (number,timestamp) VALUES ({n},{int(round(time.time() * 1000))});"))
        conn.commit()

def get_last_row():
    # Retrieve the last number inserted inside the 'numbers'
    query = sql.text("" + \
            "SELECT number " + \
            "FROM numbers " + \
            "WHERE timestamp >= (SELECT max(timestamp) FROM numbers)" + \
            "LIMIT 1")

    with engine.connect() as conn:
        result_set = conn.execute(query)  
        for (r) in result_set:  
            return r[0]

if __name__ == '__main__':
    print('Application started')
    
    while True:
        time.sleep(5)
        add_new_row(random.randint(1,100000))
        print('The last value insterted is: {}'.format(get_last_row()))