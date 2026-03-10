from flask import Flask, request, jsonify, render_template
import mysql.connector
import qrcode
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jboo7as@",   # your password
    database="metro_ticket_system"
)

cursor = db.cursor(dictionary=True)


# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# REGISTER PAGE
@app.route("/register-page")
def register_page():
    return render_template("register.html")


# LOGIN PAGE
@app.route("/login-page")
def login_page():
    return render_template("login.html")


# BOOK PAGE
@app.route("/book-page")
def book_page():
    return render_template("book_ticket.html")


# SHOW TICKET
@app.route("/ticket/<int:ticket_id>")
def ticket_page(ticket_id):

    query = """
    SELECT t.ticket_id,
           s1.station_name AS from_station,
           s2.station_name AS to_station,
           t.travel_date,
           t.fare
    FROM ticket t
    JOIN station s1 ON t.from_station = s1.station_id
    JOIN station s2 ON t.to_station = s2.station_id
    WHERE t.ticket_id=%s
    """

    cursor.execute(query,(ticket_id,))
    ticket = cursor.fetchone()

    # QR CODE DATA
    qr_data = f"Ticket:{ticket['ticket_id']} | {ticket['from_station']} → {ticket['to_station']}"

    img = qrcode.make(qr_data)

    qr_path = f"static/qr_{ticket_id}.png"

    img.save(qr_path)

    return render_template("ticket.html",ticket=ticket,qr=qr_path)


# VIEW ALL TICKETS
@app.route("/my-tickets/<int:passenger_id>")
def my_tickets(passenger_id):

    query = """
    SELECT t.ticket_id,
           s1.station_name AS from_station,
           s2.station_name AS to_station,
           t.travel_date,
           t.fare
    FROM ticket t
    JOIN station s1 ON t.from_station = s1.station_id
    JOIN station s2 ON t.to_station = s2.station_id
    WHERE t.passenger_id=%s
    """

    cursor.execute(query,(passenger_id,))
    tickets = cursor.fetchall()

    return render_template("tickets.html",tickets=tickets)


# REGISTER API
@app.route("/register",methods=["POST"])
def register():

    data=request.get_json()

    username=data["username"]
    email=data["email"]
    password=data["password"]

    query="INSERT INTO user(username,email,password) VALUES(%s,%s,%s)"

    cursor.execute(query,(username,email,password))
    db.commit()

    user_id=cursor.lastrowid

    # create passenger automatically
    passenger_query="""
    INSERT INTO passenger(user_id,name)
    VALUES(%s,%s)
    """

    cursor.execute(passenger_query,(user_id,username))
    db.commit()

    return jsonify({"message":"User registered successfully"})


# LOGIN API
@app.route("/login",methods=["POST"])
def login():

    data=request.get_json()

    email=data["email"]
    password=data["password"]

    query="""
    SELECT u.user_id,p.passenger_id
    FROM user u
    JOIN passenger p ON u.user_id=p.user_id
    WHERE u.email=%s AND u.password=%s
    """

    cursor.execute(query,(email,password))

    user=cursor.fetchone()

    if user:

        return jsonify({
            "message":"Login successful",
            "user":user
        })

    return jsonify({"message":"Invalid login"})


# GET STATIONS
@app.route("/stations")
def stations():

    cursor.execute("SELECT * FROM station")

    stations=cursor.fetchall()

    return jsonify(stations)


# BOOK TICKET
@app.route("/book-ticket",methods=["POST"])
def book_ticket():

    data=request.get_json()

    passenger_id=data.get("passenger_id")
    from_station=data.get("from_station")
    to_station=data.get("to_station")
    travel_date=data.get("travel_date")

    if not passenger_id:
        return jsonify({"message":"Please login first"}),401

    if not from_station or not to_station or not travel_date:
        return jsonify({"message":"All fields required"}),400

    if from_station==to_station:
        return jsonify({"message":"From and To stations cannot be same"}),400

    fare=abs(int(to_station)-int(from_station))*10

    query="""
    INSERT INTO ticket(passenger_id,from_station,to_station,travel_date,fare)
    VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(passenger_id,from_station,to_station,travel_date,fare))

    db.commit()

    ticket_id=cursor.lastrowid

    return jsonify({
        "message":"Ticket booked successfully",
        "ticket_id":ticket_id,
        "fare":fare
    })


if __name__=="__main__":
    app.run(debug=True)