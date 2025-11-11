import sys
import json
from PyQt5.QtWidgets import *

def add_student(window):
    dialog = QDialog(window)
    dialog.setWindowTitle('Add Student')
    dialog.setGeometry(800, 400, 500, 200)

    form_layout = QFormLayout()

    name_input = QLineEdit()
    lname_input = QLineEdit()
    roll_no_input = QLineEdit()
    dob_input = QLineEdit()
    sport_input = QLineEdit()
    subject_input = QLineEdit()

    form_layout.addRow('First Name:', name_input)
    form_layout.addRow('Last Name:', lname_input)
    form_layout.addRow('Roll Number:', roll_no_input)
    form_layout.addRow('Date Of Birth (YYYY-MM-DD):', dob_input)
    form_layout.addRow('Favourite Sport:', sport_input)
    form_layout.addRow('Favourite Subject:', subject_input)

    submit_button = QPushButton('Submit')
    form_layout.addRow(submit_button)

    submit_button.setStyleSheet('background-color: green; color: white')
    submit_button.move(200, 150)
    dialog.setLayout(form_layout)

    submit_button.clicked.connect(
        
        lambda: submit_form(dialog, name_input, lname_input, roll_no_input, dob_input, sport_input, subject_input)
    )

    dialog.exec_()


def submit_form(dialog, fname, lname, roll, dob, sport, subject):
 
    fname_val = fname.text().strip()
    lname_val = lname.text().strip()
    roll_val = roll.text().strip()
    dob_val = dob.text().strip()
    sport_val = sport.text().strip()
    subject_val = subject.text().strip()


    QMessageBox.information(
        dialog, "Form Data",
        f"Roll No: {roll_val}\n"
        f"First Name: {fname_val}\n"
        f"Last Name: {lname_val}\n"
        f"DOB: {dob_val}\n"
        f"Sport: {sport_val}\n"
        f"Subject: {subject_val}"
    )

    if not fname_val or not lname_val or not roll_val:
        QMessageBox.warning(
            dialog, "Missing Data",
            "First Name, Last Name, and Roll Number are mandatory fields."
        )
        return
    
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({
        "name": fname_val,
        "lname": lname_val,
        "roll_no": roll_val,
        "Date_of_Birth": dob_val,
        "Favourite_Sport": sport_val,
        "Favourite_subject": subject_val
    })

    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)

    dialog.accept() 
