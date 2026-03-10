# 🚇 Metro Ticket Booking System

A **Flask-based web application** for booking metro tickets.
This project demonstrates **DBMS concepts such as database design, relational schemas, foreign keys, and CRUD operations** using MySQL.

The system allows users to register, log in, book metro tickets, and view their tickets with a QR code.

---

# 📌 Features

* User Registration
* User Login
* Metro Ticket Booking
* Automatic Fare Calculation
* QR Code Ticket Generation
* Ticket Retrieval
* Kochi Metro Station Database

---

# 🛠 Tech Stack

Backend

* Python
* Flask

Database

* MySQL

Frontend

* HTML
* CSS
* JavaScript

Libraries

* qrcode
* pillow
* mysql-connector-python

---

# 📂 Project Structure

```
metro_ticket_system
│
├── app.py
├── database.sql
├── requirements.txt
├── README.md
│
├── templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── book_ticket.html
│   └── ticket.html
│
└── static
    └── style.css
```

---

# ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/vishu1-2/metro-ticket-booking-system.git
cd metro-ticket-booking-system
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Setup Database

Open MySQL and run:

```
database.sql
```

This will create:

* metro_db database
* required tables
* sample Kochi metro stations

---

### 4️⃣ Configure Database Connection

Inside `app.py`, update your MySQL credentials:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="metro_db"
)
```

---

### 5️⃣ Run the Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🗄 Database Schema

Main entities used:

* User
* Passenger
* Station
* Route
* Ticket
* Payment

These entities demonstrate relational database concepts such as:

* Primary Keys
* Foreign Keys
* One-to-Many relationships

---

# 🎟 Ticket System

When a user books a ticket:

1. Stations are selected
2. Fare is automatically calculated
3. Ticket is stored in the database
4. A QR code is generated for the ticket
5. The ticket can be retrieved later

---

# 🎓 Academic Purpose

This project was developed as part of a **Database Management Systems (DBMS) mini project** to demonstrate:

* Relational database design
* SQL table creation
* Backend database connectivity
* Full-stack application development

---

# 👨‍💻 Author

Viswas Govind
