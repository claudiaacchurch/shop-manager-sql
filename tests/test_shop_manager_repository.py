from lib.shop_manager_repository import ShopManagerRepository
from lib.shop_items import ShopItem
from lib.orders import Order
from datetime import date

def is_close(a, b, rel_tol=1e-9, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def test_get_all_shop_items(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    all_shop_items = repo.all_shop_items()
    print(all_shop_items)
    assert all_shop_items == [
        ShopItem(1, 'apple', 2.99, 50),
        ShopItem(2, 'tomatoes', 5.00, 60),
        ShopItem(3, 'peach', 3.53, 48),
        ShopItem(4, 'rice', 4.67, 9)
    ]

def test_format_shop_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    format_item = repo.format_shop_item(1)
    print(format_item)
    assert format_item == "You have 50 apple(s) in stock. Price: £2.99."

def test_create_shop_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    repo.create_shop_item('plum', 1,  90)
    all_items = repo.all_shop_items()
    assert all_items[-1] == ShopItem(5, 'plum', 1.00, 90)

def test_add_item_to_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    repo.assign_item_to_order(2, 3)
    result = repo.show_assigned_items()
    assert result == (2, 3)

def test_all_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    result = repo.all_orders()
    assert result  == [
        Order(1, 'claudia', date(2023, 6, 17)),
        Order(2, 'tim', date(2023, 6, 23)),
        Order(3, 'lucy', date(2023, 6, 5))
    ]

def test_create_new_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    repo.create_order('tony', '2023-08-13')
    all_orders = repo.all_orders()
    assert all_orders[-1] == Order(4, 'tony', date(2023, 8, 13))

    
def test_find_items_by_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repo = ShopManagerRepository(db_connection)
    result = repo.find_items_by_order(1)
    assert result == Order(1, 'claudia', date(2023, 6, 17), [
        ShopItem(1, 'apple', 2.99, 50),
        ShopItem(2, 'tomatoes', 5.00, 60),
        ShopItem(3, 'peach', 3.53, 48),
        ShopItem(4, 'rice', 4.67, 9)
    ])
