# 🧑‍🎓 Student Management System (Python + PyQt5)

![GitHub repo size](https://img.shields.io/github/repo-size/yourusername/student-dataset?color=blue)
![GitHub stars](https://img.shields.io/github/stars/yourusername/student-dataset?style=social)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Built with](https://img.shields.io/badge/Built%20with-JSON%20%7C%20Node.js%20%7C%20Python-orange)
![Status](https://img.shields.io/badge/Status-Active-success)



This is a **Student Panel Application** built using **Python** and **PyQt5**, providing a simple and interactive GUI to manage student records.  
The system allows users to **Add**, **Edit**, **Delete**, and **View** student details in a tabular format.

---

## 🚀 Features

✅ **Add Student** – Add new student details to the record  
✏️ **Edit Student** – Update existing student information  
🗑️ **Delete Student** – Remove student data easily  
📋 **Display Students** – View all students in a table format  
📂 **JSON Data Integration** – Load and manage student data from JSON file  
🎨 **PyQt5 GUI** – Modern, user-friendly, and responsive design  

---

## 🧰 Tech Stack

- 🐍 **Language:** Python  
- 🪟 **Framework:** PyQt5  
- 📦 **Modules Used:**
  - `PyQt5.QtWidgets`
  - `PyQt5.QtGui`
  - `PyQt5.QtCore`
- 🧩 **Custom Routes:**
  - `routes/add.py` → Add Student
  - `routes/edit.py` → Edit Student
  - `routes/delete.py` → Delete Student
  - `routes/table.py` → Load Students

---

## 🗂 Folder Structure

```

student-management-system/
│
├── main.py
├── routes/
│   ├── add.py
│   ├── edit.py
│   ├── delete.py
│   └── table.py
├── assets/
│   └── download.jpeg
└── data/
└── students.json

````

---

## 🧾 Sample JSON Data

A sample `students.json` file is included to demonstrate data integration:

```json
[
    {
        "name": "Rohan",
        "lname": "Gupta",
        "roll_no": "01",
        "Date_of_Birth": "1960-10-10",
        "Favourite_Sport": "Football",
        "Favourite_subject": "English"
    },
    {
        "name": "Aarav",
        "lname": "Patel",
        "roll_no": "102",
        "Date_of_Birth": "2008-07-19",
        "Favourite_Sport": "Football",
        "Favourite_subject": "Science"
    }
]
````

You can easily extend this file with more student records.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iamdeepak199/-Student-Management-System-Python-PyQt5-.git
cd -Student-Management-System-Python-PyQt5-
```

### 2️⃣ Install dependencies

```bash
pip install PyQt5
```

### 3️⃣ Run the application

```bash
python main.py
```

---

## 🖼 GUI Preview

🪟 The main interface includes:

* A **header** showing *“Students Record!”*
* A **QTableWidget** displaying all students
* Three **buttons** for `Add`, `Edit`, and `Delete` (color-coded)

| Action    | Color  |
| :-------- | :----- |
| 🟢 Add    | Green  |
| 🟠 Edit   | Orange |
| 🔴 Delete | Red    |

---

## 🚧 Future Enhancements

* 💾 Database integration (MySQL/SQLite)
* 🔍 Search & filter feature
* 📤 Export data to CSV/PDF
* 🔐 User authentication system

---

## 👨‍💻 Author

**Deepak Bhardwaj**
📧 [Email Me](mailto:your-email@example.com)
🌐 [GitHub Profile](https://github.com/iamdeepak199)

---

## 🏷 License

This project is licensed under the **MIT License** – feel free to use and modify it for learning or development.

---

⭐ If you like this project, don’t forget to **star** the repository on GitHub!
