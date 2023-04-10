import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

def to_string(student: dict) -> str:
    line = student["email"] + "," + student["fname"] + "," + student["lname"] + "," + str(student["points"])
    if student["grade"] != "": line.join(str(student["grade"]) + "," + student["status"])
    return line

def add_student(students: list, student: dict) -> bool:
    for s in students:
        if student["email"] == s["email"]: return False
    
    students.append(student)
    return True

def autograde(students: list):
    for student in students:
        if student["status"] == "":
            if   student["points"] > 90:    student["grade"] = 5
            elif student["points"] > 80:    student["grade"] = 4.5
            elif student["points"] > 70:    student["grade"] = 4
            elif student["points"] > 60:    student["grade"] = 3.5
            elif student["points"] > 50:    student["grade"] = 3
            else:                           student["grade"] = 2

            student["status"] = "GRADED"

def autosend(students: list):
    for student in students:
        if student["status"] == "MAILED": continue

        send_email("Grade", student["grade"], "system@school.edu.pl", student["email"], "password")

def load_data(filename: str, target: list):
    with open(filename) as f:
        for line in f:
            data = line.split(',')
            student = {
                "email" :  data[0],
                "fname" :  data[1],
                "lname" :  data[2],
                "points" : int(data[3]),
                "grade" :  float(data[4]) if len(data) > 4 else "",
                "status" : data[5].rstrip() if len(data) > 5 else ""
            }
            target.append(student)

def save_data(filename: str, source: list):
    with open(filename, "w") as f:
        for student in source:
            f.write(to_string(student))
            f.write("\n")

students = []
load_data("C5/students.txt", students)
autograde(students)

for student in students:
    print(student)

save_data("C5/students.txt", students)