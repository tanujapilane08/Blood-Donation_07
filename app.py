from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)



# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Jobs Page - Fetch jobs from database
@app.route("/jobs")
def jobs():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT job_title, company, location FROM jobs")
    jobs_list = cursor.fetchall()
    conn.close()
    
    return render_template("jobs.html", jobs=jobs_list)

# Admin Page - Add Jobs

ADMIN_PASSWORD = "admin123"  # Change this to your actual password

@app.route("/admin", methods=["GET", "POST"])
def admin():
    error = None  # Default: No error

    if request.method == "POST":
        password = request.form.get("password")
        if password != ADMIN_PASSWORD:
            error = "Incorrect Admin Password. Please try again."

    return render_template("admin.html", error=error)

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
