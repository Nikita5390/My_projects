import json
from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)

DB_HOST = "localhost"
DB_NAME = "my_db"
DB_USER = "postgres"
DB_PASS = "1"
TB_NAME = "my_data"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/', methods=['GET', 'POST'])
def index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    message = ''
    if request.method == 'POST':
        cur.execute(
        f"CREATE TABLE {TB_NAME}( id UUID PRIMARY KEY DEFAULT gen_random_uuid(), Email JSONB")
        conn.commit()
        my_data = request.form.getlist('field[]')
        for value in my_data:
            value = json.dumps(value)
            cur.execute(f"INSERT INTO {TB_NAME} (Email) VALUES (%s::jsonb)", [value])
            conn.commit()
        cur.close()
        message = "Info added successfully"
    if request.method == 'GET':
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(f"SELECT * FROM {TB_NAME}")
        message = cur.fetchall()
        cur.close()
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
