from flask import Flask, render_template, request, redirect, url_for
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
    error = None  # Default error value

    if request.method == "POST":
        password = request.form.get("password")
        if password != ADMIN_PASSWORD:
            error = "Incorrect Admin Password. Please try again."
        else:
            job_title = request.form.get("job_title")
            company = request.form.get("company")
            location = request.form.get("location")

            if job_title and company and location:
                conn = sqlite3.connect("jobs.db")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO jobs (job_title, company, location) VALUES (?, ?, ?)", 
                               (job_title, company, location))
                conn.commit()
                conn.close()

                return redirect(url_for("jobs"))
            else:
                error = "All fields are required to add a job."
            print(error) 

    return render_template("admin.html", error=error)  # Ensure error is passed


  

# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
