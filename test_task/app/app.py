from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Database connection details (replace with your actual details or use environment variables)
DB_HOST = os.environ.get('DATABASE_HOST')
DB_NAME = os.environ.get('DATABASE_NAME')
DB_USER = os.environ.get('DATABASE_USER')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DB_PORT = "5432"

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        #connection_status = "Connected successfully!"
        cur = conn.cursor()
        # Example: Execute a query
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        conn.close()
    except Exception as e:
        connection_status = f"Connection failed: {e}"
    
    return render_template('index.html', status=db_version)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)