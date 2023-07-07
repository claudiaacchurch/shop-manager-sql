from lib.shop_items import ShopItem

def test_shop_item_construction():
    shop_item = ShopItem(1, 'apple', 2.99, 50)
    assert shop_item.id == 1
    assert shop_item.name == 'apple'
    assert shop_item.unit_price == 2.99
    assert shop_item.quantity == 50

def test_eq_method_asserts_equal_two_same_details():
    shop_item = ShopItem(1, 'apple', 2.99, 50)
    shop_item1 = ShopItem(1, 'apple', 2.99, 50)
    assert shop_item == shop_item1
    
def test_decimal_formats_two_zeros():
    shop_item = ShopItem(1, 'apple', 2.00, 50)
    assert shop_item.unit_price == 2.00

def test_repr_formats_string():
    shop_item = ShopItem(1, 'apple', 2.00, 50)
    assert str(shop_item) == "ShopItem(1, apple, 2.00, 50)" 