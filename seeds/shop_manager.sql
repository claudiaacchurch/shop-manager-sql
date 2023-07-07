DROP TABLE IF EXISTS shop_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS shop_items_orders;

CREATE TABLE shop_items (
    id SERIAL PRIMARY KEY,
    name TEXT,
    unit_price FLOAT,
    quantity INT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name TEXT,
    date_placed date
);

CREATE TABLE shop_items_orders (
    shop_item_id INT,
    order_id INT,
    constraint fk_shop_item foreign key(shop_item_id) 
    references shop_items(id) on delete cascade,
    constraint fk_order foreign key(order_id)
    references orders(id) on delete cascade,
    PRIMARY KEY (shop_item_id, order_id)
);

INSERT INTO shop_items (name, unit_price, quantity) VALUES ('apple', 2.99, 50);
INSERT INTO shop_items (name, unit_price, quantity) VALUES ('tomatoes', 5.00, 60);
INSERT INTO shop_items (name, unit_price, quantity) VALUES ('peach', 3.53, 48);
INSERT INTO shop_items (name, unit_price, quantity) VALUES ('rice', 4.67, 9);
INSERT INTO orders (customer_name, date_placed) VALUES ('claudia', '2023-6-17');
INSERT INTO orders (customer_name, date_placed) VALUES ('tim', '2023-6-23');
INSERT INTO orders (customer_name, date_placed) VALUES ('lucy', '2023-6-5');
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (1, 1);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (2, 1);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (3, 1);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (4, 1);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (1, 2);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (3, 2);
INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (1, 3);

