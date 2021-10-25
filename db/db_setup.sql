CREATE DATABASE cafe_app;

CREATE TABLE products (
product_id INT NOT NULL AUTO_INCREMENT,
product_name VARCHAR(255) NOT NULL,
product_price DOUBLE NOT NULL,
product_stock INT NOT NULL,
PRIMARY KEY(product_id)
);

CREATE TABLE couriers (
courier_id INT NOT NULL AUTO_INCREMENT,
courier_name VARCHAR(255) NOT NULL,
courier_phone VARCHAR(255) NOT NULL,
PRIMARY KEY(courier_id)
);

CREATE TABLE customers (
customer_id INT NOT NULL AUTO_INCREMENT,   
customer_name VARCHAR(255) NOT NULL,
customer_address VARCHAR(255) NOT NULL,
customer_phone VARCHAR(255) NOT NULL,
PRIMARY KEY(customer_id)
);

CREATE TABLE order_status (
order_status_id INT NOT NULL AUTO_INCREMENT,
order_status VARCHAR(255) NOT NULL,
PRIMARY KEY(order_status_id)
);

CREATE TABLE orders (
order_id INT NOT NULL AUTO_INCREMENT,
customer_id INT NOT NULL, 
courier_id INT NOT NULL,
order_status_id INT NOT NULL,
order_total_cost DOUBLE,
PRIMARY KEY(order_id),
FOREIGN KEY(customer_id) REFERENCES customers (customer_id),
FOREIGN KEY(courier_id) REFERENCES couriers (courier_id),
FOREIGN KEY(order_status_id) REFERENCES order_status (order_status_id)
);

CREATE TABLE order_products (
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT NOT NULL,
PRIMARY KEY (order_id, product_id),
FOREIGN KEY (order_id) REFERENCES orders (order_id),
FOREIGN KEY (product_id) REFERENCES products (product_id)
);

INSERT INTO products (product_name, product_price, product_stock)
VALUES ('Coke', 1.25, 12), ('Fanta', 0.75, 15), ('Pepsi', 1, 20); 

INSERT INTO couriers (courier_name, courier_phone)
VALUES ('Mike', '07459346523'), ('Pete', '07459346523'), ('Claire', '07459346523');

INSERT INTO customers (customer_name, customer_address, customer_phone)
VALUES ('Pete', 'Standard Avenue, Covenrty', '07429246100'),
('Kevin', 'Oxford Street, London', '07457582365'),
('Claire', 'Balsall Common, Warwickshire', '07775505500');

INSERT INTO order_status (order_status)
VALUES ('preparing'), ('out-for-delivery'), ('delivered');