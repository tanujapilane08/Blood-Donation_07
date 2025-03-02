from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

ADMIN_PASSWORD = "admin123"  # Change this to your desired password

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
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        password = request.form.get("password")
        job_title = request.form.get("job_title")
        company = request.form.get("company")
        location = request.form.get("location")

        if password == ADMIN_PASSWORD:
            conn = sqlite3.connect("jobs.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO jobs (job_title, company, location) VALUES (?, ?, ?)", 
                           (job_title, company, location))
            conn.commit()
            conn.close()

            return "<h3>Job added successfully!</h3><a href='/jobs'>View Jobs</a>"
        else:
            return render_template("admin.html", error="Incorrect Password")

    return render_template("admin.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
