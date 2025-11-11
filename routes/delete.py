from PyQt5.QtWidgets import QInputDialog, QMessageBox
import json

def delete_student(window):
    roll_no, ok = QInputDialog.getInt(window, 'Delete Student', 'Enter roll number to delete:')
    if not ok:
        return

    try:
        with open('students.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        QMessageBox.warning(window, 'Error', 'No student records found.')
        return

    # Convert to string for comparison
    roll_no_str = str(roll_no)

    new_data = [student for student in data if student.get('roll_no') != roll_no_str]

    if len(new_data) == len(data):
        QMessageBox.information(window, 'Not Found', 'Student not found.')
        return

    with open('students.json', 'w') as f:
        json.dump(new_data, f, indent=4)

    QMessageBox.information(window, 'Deleted', 'Student deleted successfully.')
