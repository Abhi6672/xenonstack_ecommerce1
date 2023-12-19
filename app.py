from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace these with your actual MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'N#@98wrft45',
    'database': 'newtask'
}


def insert_data(name, email):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Example query to insert data into a 'users' table
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(query, values)

        connection.commit()
        print("Data inserted successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        email = request.form['email']

        # Insert data into MySQL
        insert_data(name, email)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
