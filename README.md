# Employee Management System

![Employee Management System](https://img.shields.io/badge/Django-4.2.7-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow) ![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

A **Full-Stack Employee Management System** built using **Django, DataTables, JavaScript, and Bootstrap**, designed to manage employee records efficiently.

## 🚀 Features

### **🔹 Admin Panel**
- Manage employees (Add, Edit, Delete)
- Update employee **Education Details**
- Manage employee **Experience Details**
- Assign roles & permissions

### **🔹 Employee Management**
- View employee list (with search & sorting)
- CRUD operations for employees
- Add/Edit education & experience details
- Delete employee records

### **🔹 User Authentication**
- Secure **login/logout** system
- Role-based access control

### **🔹 Interactive Dashboard**
- Employee statistics & analytics
- Real-time search & filtering using **DataTables**

## 🛠 Tech Stack

### **Backend**
- **Django** (Python Web Framework)
- **Django REST Framework** (API handling)
- **SQLite / PostgreSQL** (Database Management)

### **Frontend**
- **HTML, CSS, JavaScript**
- **Bootstrap 5** (Responsive UI)
- **DataTables.js** (Advanced table functionalities)

### **Libraries & Dependencies**
- **jQuery** (Event handling & AJAX requests)
- **Django Auth** (User authentication & session handling)
- **Django Templates** (Server-side rendering)

## 📂 Project Structure
```bash
Employee_Management_System/
│── employee_mgmt/             # Main Django App
│   ├── models.py              # Database Models
│   ├── views.py               # Business Logic & API Endpoints
│   ├── urls.py                # URL Routing
│   ├── forms.py               # Django Forms
│   ├── templates/             # HTML Templates
│── static/                    # CSS, JS, Images
│── db.sqlite3                 # Database File
│── manage.py                  # Django Management Script
│── README.md                  # Project Documentation
```

## ⚙️ Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Kartikjoshi14/Employee_Management_System_py.git
cd Employee_Management_System_py
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Apply Migrations & Run the Server**
```bash
python manage.py migrate
python manage.py runserver
```

### **4️⃣ Access the App**
- Open **http://127.0.0.1:8000/** in your browser

## 🎯 Future Enhancements
- ✅ Employee Performance Tracking
- ✅ Attendance Management
- ✅ Export Data to CSV/PDF
- ✅ Notifications & Email Alerts

## 🤝 Contributing
Pull requests are welcome! Feel free to **fork** this repository and submit PRs.

## 📜 License
This project is licensed under the **MIT License**.

---
🚀 **Developed by [Kartik Joshi](https://github.com/Kartikjoshi14)**

