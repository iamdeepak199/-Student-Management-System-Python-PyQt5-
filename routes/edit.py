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
    for student in data:
        if student.get('roll_no') == roll_val:
            QMessageBox.warning(dialog, 'Duplicate Roll No', 'A student with this roll number already exists.')
            return  
    student = {
        'name': fname_val,
        'lname': lname_val,
        'roll_no': roll_val,
        'Date_of_Birth': dob_val,
        'Favourite_Sport': sport_val,
        'Favourite_subject': subject_val
    }   
    data.append(student)
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)
    dialog.accept()
def edit_student(window):
    roll_no, ok = QInputDialog.getText(window, 'Edit Student', 'Enter roll number to edit:')
    if not ok or not roll_no:
        return     
    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []    
    for student in data:
        if student.get('roll_no') == roll_no:
            break   
    else:
        QMessageBox.information(window, 'Not Found', 'Student not found.')
        return
    dialog = QDialog(window)
    dialog.setWindowTitle('Edit Student')
    dialog.setGeometry(800, 400, 500, 200)
    form_layout = QFormLayout()
    name_input = QLineEdit(student.get('name', ''))
    lname_input = QLineEdit(student.get('lname', ''))
    roll_no_input = QLineEdit(student.get('roll_no', ''))

    dob_input = QLineEdit(student.get('Date_of_Birth', '')) 
    sport_input = QLineEdit(student.get('Favourite_Sport', ''))
    subject_input = QLineEdit(student.get('Favourite_subject', ''))

    form_layout.addRow('First Name:', name_input)
    form_layout.addRow('Last Name:', lname_input)
    form_layout.addRow('Roll Number:', roll_no_input)
    form_layout.addRow('Date Of Birth (YYYY-MM-DD):', dob_input)
    form_layout.addRow('Favourite Sport:', sport_input)
    form_layout.addRow('Favourite Subject:', subject_input)
    submit_button = QPushButton('Update')
    form_layout.addRow(submit_button)
    submit_button.setStyleSheet('background-color: orange; color: white')
    submit_button.move(200, 150)
    dialog.setLayout(form_layout)
    submit_button.clicked.connect(
        lambda: update_student(dialog, data, roll_no, name_input, lname_input, roll_no_input, dob_input, sport_input, subject_input)
    )
    dialog.exec_()
def update_student(window, data, roll_no, fname, lname, roll_input, dob, sport, subject):
    fname_val = fname.text().strip()
    lname_val = lname.text().strip()
    roll_val = roll_input.text().strip()


    dob_val = dob.text().strip()
    sport_val = sport.text().strip()
    subject_val = subject.text().strip()
    if not fname_val or not lname_val or not roll_val:
        QMessageBox.warning(
            window, "Missing Data",
            "First Name, Last Name, and Roll Number are mandatory fields."
        )
        return
    for student in data:
        if student.get('roll_no') == roll_no:
            student['name'] = fname_val
            student['lname'] = lname_val
            student['roll_no'] = roll_val
            student['Date_of_Birth'] = dob_val
            student['Favourite_Sport'] = sport_val
            student['Favourite_subject'] = subject_val
            break
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)    
    window.accept()
    QMessageBox.information(window, 'Success', 'Student record updated successfully.')

    return
