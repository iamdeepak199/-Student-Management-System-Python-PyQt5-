from PyQt5.QtWidgets import * 
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from routes.add import add_student
from routes.delete import delete_student
from routes.edit import edit_student
from routes.table import load_students

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Student Management System')
window.setWindowIcon(QIcon('download.jpeg'))
window.fullscreen = True

label = QLabel('<h1>Students Record :!</h1>', parent=window)
label.setFont(QFont('Arial', 10))
label.setStyleSheet('color: blue')
label.setAlignment(Qt.AlignHCenter)
label.move(60, 30)

table = QTableWidget(parent=window)
table.setGeometry(100, 100, 910, 200)
load_students(table)

button1 = QPushButton('Add', parent=window)
button2 = QPushButton('Edit', parent=window)
button3 = QPushButton('Delete', parent=window)

button1.setStyleSheet('background-color: green; color: white')
button2.setStyleSheet('background-color: orange; color: white')
button3.setStyleSheet('background-color: red; color: white')

button1.move(100, 350)
button2.move(300, 350)
button3.move(500, 350)

def add_and_reload():
    add_student(window)
    load_students(table)

def delete_and_reload():
    delete_student(window)
    load_students(table)


button1.clicked.connect(add_and_reload)
button2.clicked.connect(lambda: [edit_student(window), load_students(table)])
button3.clicked.connect(delete_and_reload)

window.show()
sys.exit(app.exec_())

