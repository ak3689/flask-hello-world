import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from --Ahmed Khan-- in 3308'


@app.route('/db_test')
def testing():
    conn = psycopg2.connect(postgresql://ahmed_render_db_user:UGqZ1UOcGpoRVW10SSVWHeUqhHNlWVEf@dpg-cvjchvripnbc73e1cqkg-a/ahmed_render_db)
    conn.close()
    return "Database connection successful"
