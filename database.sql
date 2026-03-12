-- Create Database
CREATE DATABASE IF NOT EXISTS metro_db;
USE metro_db;


-- USER TABLE
CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'passenger',
    PRIMARY KEY (user_id),
    UNIQUE KEY username (username),
    UNIQUE KEY email (email)
);


-- PASSENGER TABLE
CREATE TABLE passenger (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    phone VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);


-- STATION TABLE
CREATE TABLE station (
    station_id INT NOT NULL AUTO_INCREMENT,
    station_name VARCHAR(100) NOT NULL,
    location VARCHAR(100),
    PRIMARY KEY (station_id)
);


-- ROUTE TABLE
CREATE TABLE route (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    route_name VARCHAR(100),
    start_station INT,
    end_station INT,
    FOREIGN KEY (start_station) REFERENCES station(station_id),
    FOREIGN KEY (end_station) REFERENCES station(station_id)
);


-- TICKET TABLE
CREATE TABLE ticket (
    ticket_id INT NOT NULL AUTO_INCREMENT,
    passenger_id INT,
    travel_date DATE,
    fare INT,
    from_station INT,
    to_station INT,
    PRIMARY KEY (ticket_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
    FOREIGN KEY (from_station) REFERENCES station(station_id),
    FOREIGN KEY (to_station) REFERENCES station(station_id)
);


-- PAYMENT TABLE
CREATE TABLE payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT,
    amount INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id)
);


-- SAMPLE KOCHI METRO STATIONS
INSERT INTO station (station_name, location) VALUES
('Aluva','Kochi'),
('Pulinchodu','Kochi'),
('Companypady','Kochi'),
('Ambattukavu','Kochi'),
('Muttom','Kochi'),
('Kalamassery','Kochi'),
('CUSAT','Kochi'),
('Pathadipalam','Kochi'),
('Edapally','Kochi'),
('Changampuzha Park','Kochi'),
('Palarivattom','Kochi'),
('JLN Stadium','Kochi'),
('Kaloor','Kochi'),
('Town Hall','Kochi'),
('MG Road','Kochi'),
('Maharajas College','Kochi'),
('Ernakulam South','Kochi'),
('Kadavanthra','Kochi'),
('Elamkulam','Kochi'),
('Vyttila','Kochi');