from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mydatabase",
        user="mydbuser",
        password="MyDBPassword",
        host="10.0.0.5",
        port="5432"
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    users = []
    search_performed = False  # Flag to indicate if search was performed
    if request.method == 'POST':
        search_term = request.form.get('search', '').strip()
        if search_term:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE first_name LIKE %s OR last_name LIKE %s",
                           (f'%{search_term}%', f'%{search_term}%'))
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            search_performed = True  # Set flag to True after search
    return render_template('index.html', users=users, search_performed=search_performed)

if __name__ == '__main__':
    app.run(debug=True)
