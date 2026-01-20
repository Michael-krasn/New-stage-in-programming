from src.models import Product, Category

def test_average_price_with_products():
    p1 = Product("A", "desc", 100, 1)
    p2 = Product("B", "desc", 300, 1)
    cat = Category("ТестКатегория", "Описание", [p1, p2])
    assert cat.average_price() == 200

def test_average_price_empty_category():
    cat = Category("Пустая", "Описание")
    assert cat.average_price() == 0