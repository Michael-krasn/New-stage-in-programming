import pytest

from src.models import (
    Category,
    CategoryIterator,
    LawnGrass,
    Order,
    Product,
    Smartphone,
)

# ---------- Product ----------


def test_product_creation():
    product = Product("Телефон", "Описание", 1000, 5)
    assert product.name == "Телефон"
    assert product.description == "Описание"
    assert product.price == 1000
    assert product.quantity == 5


def test_product_price_private():
    product = Product("Товар", "Описание", 1000, 1)
    assert not hasattr(product, "price__")
    assert product.price == 1000


def test_product_price_setter_negative(capsys):
    product = Product("Товар", "Описание", 1000, 1)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 1000


def test_product_str():
    product = Product("Товар", "Описание", 100, 3)
    assert str(product) == "Товар, 100 руб. Остаток: 3 шт."


def test_product_add_same_type():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert p1.add(p2) == 100 * 2 + 200 * 3


def test_product_add_different_type():
    product = Product("Товар", "Описание", 100, 1)
    phone = Smartphone("iPhone", "Описание", 1000, 1, 90, "15 Pro", "256GB", "Gray")
    with pytest.raises(TypeError):
        product.add(phone)


# ---------- Smartphone / LawnGrass ----------


def test_smartphone_add():
    s1 = Smartphone("Phone1", "Desc", 1000, 2, 90, "X", "128GB", "Black")
    s2 = Smartphone("Phone2", "Desc", 1200, 3, 95, "Y", "256GB", "White")
    assert s1.add(s2) == 5


def test_lawngrass_add():
    g1 = LawnGrass("Grass1", "Desc", 100, 5, "RU", 10, "Green")
    g2 = LawnGrass("Grass2", "Desc", 120, 7, "RU", 12, "Dark green")
    assert g1.add(g2) == 12


# ---------- Category ----------


def test_category_creation():
    product = Product("Товар", "Описание", 100, 2)
    category = Category("Категория", "Описание", [product])

    assert category.name == "Категория"
    assert len(category.products) == 1


def test_add_product_to_category():
    category = Category("Категория", "Описание")
    product = Product("Товар", "Описание", 100, 3)

    category.add_product(product)

    assert category.products[0] == product


def test_add_not_product_to_category():
    category = Category("Категория", "Описание")
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_category_str():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    category = Category("Категория", "Описание", [p1, p2])

    assert category.str() == "Категория, количество продуктов: 5 шт."


def test_category_total_price():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    category = Category("Категория", "Описание", [p1, p2])

    assert category.total_price() == 100 * 2 + 200 * 3


# ---------- CategoryIterator ----------


def test_category_iterator():
    p1 = Product("Товар1", "Описание", 100, 1)
    p2 = Product("Товар2", "Описание", 200, 1)
    category = Category("Категория", "Описание", [p1, p2])

    iterator = CategoryIterator(category)

    assert iterator.next() == p1
    assert iterator.next() == p2

    with pytest.raises(StopIteration):
        iterator.next()


# ---------- Order ----------


def test_order_creation_and_total_price():
    product = Product("Товар", "Описание", 500, 10)
    order = Order(product, 3)

    assert order.total_price == 1500


def test_order_not_product():
    with pytest.raises(TypeError):
        Order("не продукт", 1)
