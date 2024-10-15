from flask import Flask, jsonify, render_template
import psycopg2

app = Flask(__name__)

def get_random_row():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="mydbuser",
        password="MyDBPassword",
        host="10.0.0.5"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY random() LIMIT 1;")
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

@app.route('/')
def index():
    return render_template('index.html')  # Ensures the HTML page is served.

@app.route('/random')
def random_row():
    row = get_random_row()
    return jsonify(row)  # Serves the JSON data.

if __name__ == '__main__':
    app.run(host='0.0.0.0')
