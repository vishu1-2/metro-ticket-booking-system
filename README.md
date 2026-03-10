# 🚇 Metro Ticket Booking System

A **Flask-based web application** for booking metro tickets.
This project demonstrates **Database Management System (DBMS) concepts** such as relational database design, foreign keys, and SQL queries using MySQL.

The system allows users to register, log in, book metro tickets, and retrieve previously booked tickets with QR codes.

---

# 📌 Features

* User Registration
* User Login
* Metro Ticket Booking
* Automatic Fare Calculation
* QR Code Ticket Generation
* View Previously Booked Tickets
* Kochi Metro Station Database

---

# 🛠 Tech Stack

### Backend

* Python
* Flask

### Database

* MySQL

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

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
│   ├── ticket.html
│   └── tickets.html
│
└── static
    └── style.css
```

---

# ⚙️ Installation and Setup

## 1️⃣ Clone the Repository

```
git clone https://github.com/vishu1-2/metro-ticket-booking-system.git
cd metro-ticket-booking-system
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Setup the Database

Open MySQL and run the SQL file:

```
database.sql
```

This will create:

* `metro_ticket_system` database
* all required tables
* sample Kochi metro stations

---

## 4️⃣ Configure Database Connection

Inside `app.py`, update your MySQL credentials:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="metro_ticket_system"
)
```

---

## 5️⃣ Run the Application

```
python app.py
```

Then open your browser:

```
http://127.0.0.1:5000
```

---

# 🔗 API Endpoints

### Register User

POST `/register`

Example Request

```
{
  "username": "user1",
  "email": "user@email.com",
  "password": "password123"
}
```

---

### Login User

POST `/login`

Example Request

```
{
  "email": "user@email.com",
  "password": "password123"
}
```

---

### Get All Stations

GET `/stations`

Returns all available metro stations.

---

### Book Ticket

POST `/book-ticket`

Example Request

```
{
  "passenger_id": 1,
  "from_station": 3,
  "to_station": 8,
  "travel_date": "2026-03-15"
}
```

Example Response

```
{
  "message": "Ticket booked successfully",
  "ticket_id": 21,
  "fare": 50
}
```

---

### Get Ticket Details

GET `/ticket/<ticket_id>`

Example

```
/ticket/5
```

---

### View All Tickets of a Passenger

GET `/tickets/<passenger_id>`

Returns all previously booked tickets.

---

# 🗄 Database Entities

The system contains the following tables:

* **User** – stores login credentials
* **Passenger** – stores passenger details
* **Station** – stores metro station information
* **Route** – defines metro routes
* **Ticket** – stores ticket booking information
* **Payment** – stores payment details

These tables demonstrate relational database concepts such as:

* Primary Keys
* Foreign Keys
* One-to-Many Relationships

---

# 🎟 Ticket Booking Workflow

1. User registers an account
2. User logs into the system
3. User selects **from station** and **to station**
4. Fare is automatically calculated
5. Ticket is stored in the database
6. QR code is generated for the ticket
7. User can view previously booked tickets

---

# 🎓 Academic Purpose

This project was developed as part of a **Database Management Systems (DBMS) mini project** to demonstrate:

* Database schema design
* SQL table creation
* Backend–database integration
* Full-stack web application development

---

# 👨‍💻 Author

Viswas Govind
