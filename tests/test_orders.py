from lib.orders import Order
from datetime import date

def test_order_construction():
    order = Order(1, 'claudia', '2023-6-17')
    assert order.id == 1
    assert order.customer_name == 'claudia'
    assert order.date_placed == '2023-6-17'

def test_order_eq_method():
    order = Order(1, 'claudia', '2023-6-17')
    order2 = Order(1, 'claudia', '2023-6-17')
    assert order == order2

def test_order_repr_method():
    order = Order(1, 'claudia', '2023-6-17')
    assert str(order) == "Order(1, claudia, 2023-6-17)"