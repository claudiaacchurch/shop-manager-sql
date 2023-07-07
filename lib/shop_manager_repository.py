from lib.orders import Order
from lib.shop_items import ShopItem

class ShopManagerRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all_shop_items(self):
        rows = self._connection.execute('SELECT * FROM shop_items')
        items = []
        for row in rows:
            item = ShopItem(row['id'], row['name'], row['unit_price'], row['quantity'])
            items.append(item)
        return items
    
    def format_shop_item(self, id):
        items = self._connection.execute('SELECT * FROM shop_items WHERE id = %s', [id])
        item = items[0]
        return f"You have {item['quantity']} {item['name']}(s) in stock. Price: £{item['unit_price']}."

    def create_shop_item(self, name, unit_price, quantity):
        self._connection.execute('INSERT INTO shop_items (name, unit_price, quantity) VALUES (%s, %s, %s)', [name, unit_price, quantity])

    def show_assigned_items(self):
        rows = self._connection.execute('SELECT * FROM shop_items_orders')
        last_pair = rows[-1]
        return (last_pair['shop_item_id'], last_pair['order_id'])

    def assign_item_to_order(self, shop_item_id, order_id):
        self._connection.execute('INSERT INTO shop_items_orders (shop_item_id, order_id) VALUES (%s, %s)', [shop_item_id, order_id])
    
    def all_orders(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders = []
        for row in rows:
            order = Order(row['id'], row['customer_name'], row['date_placed'])
            orders.append(order)
        return orders
    
    #create new order
    def create_order(self, customer_name, date_placed):
        self._connection.execute('INSERT INTO orders (customer_name, date_placed) VALUES (%s, %s)', [customer_name, date_placed])

    #show all items in order
    def find_items_by_order(self, order_id):
        rows = self._connection.execute('SELECT orders.id AS order_id, orders.customer_name, orders.date_placed, '\
                                 'shop_items.id, shop_items.name, shop_items.unit_price, shop_items.quantity '\
                                    'FROM orders JOIN shop_items_orders ON shop_items_orders.order_id = orders.id '\
                                        'JOIN shop_items ON shop_items_orders.shop_item_id = shop_items.id '\
                                            'WHERE order_id = %s', [order_id])
        items = []
        for row in rows:
            item = ShopItem(row['id'], row['name'], row['unit_price'], row['quantity'])
            items.append(item)
        return Order(rows[0]['order_id'], rows[0]['customer_name'], rows[0]['date_placed'], items)