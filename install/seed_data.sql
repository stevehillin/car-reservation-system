INSERT INTO booking_status 
    (name) 
    VALUES 
        ('FUTURE'),
        ('ACTIVE'),
        ('OVERDUE');

INSERT INTO vehicle_categories 
    (name, capacity) 
    VALUES 
        ('Compact', 4),
        ('Luxury', 7),
        ('Van', 15);

INSERT INTO vehicles 
    (category_id, vin, plate, make, model, year) 
    VALUES 
        (1, 'fakevin1', 'plate1', 'Toyota', 'Corolla', 2023),
        (2, 'fakevin2', 'plate2', 'GMC', 'Suburban', 2021),
        (3, 'fakefin3', 'plate3', 'Ford', 'Econoline', 2022);

INSERT INTO customers
    (first_name, last_name, address, city, state, zip, phone, email)
    VALUES
        ('Steve', 'Hillin', '123 Anywhere Street', 'Anyplace', 'TX', '00000', '+12819875791','stevehillin+nospam@gmail.com'),
        ('Steve2', 'Hillin2', '1234 Anywhere Street', 'Anyplace', 'TX', '00000', '+12819875791','stevehillin+nospam2@gmail.com');

INSERT INTO bookings
    (customer_id, vehicle_id, hire_date, return_date, book_status)
    VALUES
        (1, 3, '2023-10-24 00:00:00', '2023-10-28 00:00:00', 1);

-- Should fail, too many days hired

INSERT INTO bookings
    (customer_id, vehicle_id, hire_date, return_date, book_status)
    VALUES
        (1, 3, '2023-10-24 00:00:00', '2023-11-02 00:00:00', 1);

-- Should fail, too far in future (Works, need to fix.)

INSERT INTO bookings
    (customer_id, vehicle_id, hire_date, return_date, book_status)
    VALUES
        (1, 3, '2023-11-24 00:00:00', '2023-11-26 00:00:00', 1);

-- Should fail, return date before hire_date

INSERT INTO bookings
    (customer_id, vehicle_id, hire_date, return_date, book_status)
    VALUES
        (1, 3, '2023-11-24 00:00:00', '2023-11-23 00:00:00', 1);