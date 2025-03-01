import tkinter as tk
from tkinter import messagebox
import time
import smtplib
from email.mime.text import MIMEText

# Configure your email credentials
EMAIL_ADDRESS ="sujaybote29@gmail.com"
EMAIL_PASSWORD = "sujay||7276||"

donors = [
    {"name": "abhishek", "blood_group": "O+", "contact": "7020469625", "email": "abhishekkapase77@gmail.com", "available": True},
    {"name": "Trupti", "blood_group": "B+", "contact": "8656977296", "email": "trupti@example.com", "available": True},
    {"name": "sujay", "blood_group": "A+", "contact": "7276239759", "email": "sujay@example.com", "available": True},
    {"name": "tanuja", "blood_group": "B-", "contact": "9322029481", "email": "tanuja@example.com", "available": False}
]

def send_email(to_email, subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        
        messagebox.showinfo("Email Sent", f"Email sent successfully to {to_email}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {e}")

def find_donor():
    bg = blood_group_entry.get()
    for donor in donors:
        if donor["blood_group"] == bg and donor["available"]:
            messagebox.showinfo("Donor Found", f"{donor['name']}, Contact: {donor['contact']}")
            send_email(donor["email"], "Urgent Blood Donation Request", f"Dear {donor['name']},\n\nAn urgent need for {bg} blood group has been reported. Please contact the nearest hospital if you can donate.\n\nThank you!")
            return
    messagebox.showwarning("No Donor Found", "No available donor for this blood group.")

def sos_alert():
    messagebox.showinfo("SOS Alert", "Notifying nearby donors and emergency contacts...")
    time.sleep(2)
    messagebox.showinfo("SOS Alert", "Alert sent successfully!")

def update_status():
    name = donor_name_entry.get()
    for donor in donors:
        if donor["name"].lower() == name.lower():
            donor["available"] = not donor["available"]
            status = "Available" if donor["available"] else "Unavailable"
            messagebox.showinfo("Status Updated", f"{donor['name']}'s status updated to {status}")
            return
    messagebox.showwarning("Error", "Donor not found.")

# GUI Setup
root = tk.Tk()
root.title("Blood Donation & Emergency Help")
root.geometry("400x300")

tk.Label(root, text="Enter Blood Group:").pack()
blood_group_entry = tk.Entry(root)
blood_group_entry.pack()
tk.Button(root, text="Search Donor", command=find_donor).pack()

tk.Label(root, text="Enter Donor Name:").pack()
donor_name_entry = tk.Entry(root)
donor_name_entry.pack()
tk.Button(root, text="Update Donor Status", command=update_status).pack()

tk.Button(root, text="Send SOS Alert", command=sos_alert).pack()

tk.Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
