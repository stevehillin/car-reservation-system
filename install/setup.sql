DROP DATABASE reserve;
CREATE DATABASE reserve;

USE reserve;

DROP USER IF EXISTS 'reserve_readonly'@'localhost';
DROP USER IF EXISTS 'reserve_admin'@'localhost';
DROP USER IF EXISTS 'reserve_superadmin'@'localhost';


CREATE USER 'reserve_readonly'@'localhost' IDENTIFIED BY '3a32fa98b86a9edb241852d22973fe73';
CREATE USER 'reserve_admin'@'localhost' IDENTIFIED BY 'ee71542ebce7996a9da406b18f597c5b';
CREATE USER 'reserve_superadmin'@'localhost' IDENTIFIED BY 'fd9b21a876a9a928526356aea856a854';
GRANT SELECT ON reserve.* to 'reserve_readonly'@'localhost';
GRANT SELECT,INSERT,CREATE,UPDATE,DELETE on reserve.* to 'reserve_admin'@'localhost';
GRANT ALL PRIVILEGES ON reserve.* to 'reserve_superadmin'@'localhost';
FLUSH PRIVILEGES;

-- Create Types and Categories

CREATE TABLE reserve.vehicle_categories (
    id tinyint unsigned not null auto_increment,
    name varchar(50) not null default '',
    capacity tinyint unsigned not null default 4,
    PRIMARY KEY (id),
    CONSTRAINT u_vc_name UNIQUE (name),
    CONSTRAINT c_capacity_check CHECK (capacity in (4, 7, 15))
);

CREATE TABLE reserve.booking_status (
    id tinyint unsigned not null auto_increment,
    name varchar(50) not null default '',
    PRIMARY KEY (id),
    CONSTRAINT u_bs_name UNIQUE (name)
);

-- Vehicles and Customers

CREATE TABLE reserve.vehicles (
    id int unsigned not null auto_increment,
    category_id tinyint unsigned not null,
    vin varchar(17) not null,
    plate varchar(10) not null,
    make varchar(100) not null,
    model varchar(100) not null,
    year int not null,
    PRIMARY KEY (id),
    CONSTRAINT u_vin UNIQUE (vin),
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES reserve.vehicle_categories (id)
);

CREATE TABLE reserve.customers (
    id int unsigned not null auto_increment,
    first_name varchar(50) not null,
    last_name varchar(100) not null,
    address varchar(100) not null,
    city varchar(100) not null,
    state varchar(2) not null,
    zip varchar(10) not null,
    phone varchar(12) not null,
    email varchar(100) not null,
    PRIMARY KEY (id),
    CONSTRAINT u_email UNIQUE (email)
);

-- Operations

CREATE TABLE reserve.bookings (
    id bigint unsigned not null auto_increment,
    customer_id int unsigned not null,
    vehicle_id int unsigned not null,
    hire_date datetime not null,
    return_date datetime not null,
    book_status tinyint unsigned not null,
    PRIMARY KEY (id),
    CONSTRAINT fk_booking_customer_id FOREIGN KEY (customer_id) REFERENCES reserve.customers (id),
    CONSTRAINT fk_booking_vehicle_id FOREIGN KEY (vehicle_id) REFERENCES reserve.vehicles (id),
    CONSTRAINT fk_booking_status FOREIGN KEY (book_status) REFERENCES reserve.booking_status (id),
    CONSTRAINT hire_before_return CHECK (hire_date < return_date),
    CONSTRAINT booking_too_long CHECK (return_date < DATE_ADD(hire_date, INTERVAL 7 DAY))
);

-- Triggers

DROP TRIGGER IF EXISTS booking_not_too_far_in_future;

DELIMITER $$

CREATE TRIGGER booking_not_too_far_in_future
BEFORE INSERT ON bookings
FOR EACH ROW
BEGIN
IF (NEW.hire_date > CURDATE() + INTERVAL 7 DAY) THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'hire_date cannot be more than 7 days in the future!';
END IF;
END $$

DELIMITER ;