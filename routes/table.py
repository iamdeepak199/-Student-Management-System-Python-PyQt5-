from PyQt5.QtWidgets import*
import json
def load_students(table):
    try:
        with open('students.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    table.setRowCount(len(data))
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels([
        "First Name", "Last Name", "Roll No", "Date of Birth", "Favourite Sport", "Favourite Subject"
    ])
    for row, student in enumerate(data):
        table.setItem(row, 0, QTableWidgetItem(student.get("name", "")))
        table.setItem(row, 1, QTableWidgetItem(student.get("lname", "")))
        table.setItem(row, 2, QTableWidgetItem(str(student.get("roll_no", ""))))
        table.setItem(row, 3, QTableWidgetItem(student.get("Date_of_Birth", "")))
        table.setItem(row, 4, QTableWidgetItem(student.get("Favourite_Sport", "")))
        table.setItem(row, 5, QTableWidgetItem(student.get("Favourite_subject", "")))
