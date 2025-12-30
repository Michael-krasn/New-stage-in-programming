import pytest

from src.models import (
    Product,
    Smartphone,
    LawnGrass,
    Category,
    Order,
)


def test_product_create():
    product = Product("Товар", "Описание", 100, 2)

    assert product.name == "Товар"
    assert product.description == "Описание"
    assert product.price == 100
    assert product.quantity == 2


def test_product_str():
    product = Product("Товар", "Описание", 100, 2)

    assert str(product) == "Товар, 100 руб. Остаток: 2 шт."


def test_product_price_negative():
    with pytest.raises(ValueError):
        Product("Товар", "Описание", -10, 1)


def test_product_add_same_type():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)

    assert p1.add(p2) == 100 * 2 + 200 * 3


def test_product_add_different_type():
    product = Product("Товар", "Описание", 100, 1)
    phone = Smartphone(
        "iPhone", "Описание", 1000, 1, 90, "15 Pro", "256GB", "Gray"
    )

    with pytest.raises(TypeError):
        product.add(phone)


def test_smartphone_add():
    s1 = Smartphone(
        "iPhone", "Описание", 1000, 1, 90, "15", "256GB", "Gray"
    )
    s2 = Smartphone(
        "iPhone", "Описание", 1000, 3, 90, "15", "256GB", "Gray"
    )

    assert s1.add(s2) == 4


def test_lawn_grass_add():
    g1 = LawnGrass(
        "Трава", "Описание", 50, 5, "RU", 10, "Зелёный"
    )
    g2 = LawnGrass(
        "Трава", "Описание", 50, 3, "RU", 10, "Зелёный"
    )

    assert g1.add(g2) == 8


def test_category_create():
    product = Product("Товар", "Описание", 100, 2)
    category = Category("Категория", "Описание", [product])

    assert category.name == "Категория"
    assert len(category.products) == 1


def test_category_add_product():
    category = Category("Категория", "Описание")
    product = Product("Товар", "Описание", 100, 3)

    category.add_product(product)

    assert len(category.products) == 1
    assert category.products[0] is product


def test_category_add_not_product():
    category = Category("Категория", "Описание")

    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_category_total_price():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 1)

    category = Category("Категория", "Описание", [p1, p2])

    assert category.total_price() == 400


def test_category_iterator():
    p1 = Product("Товар1", "Описание", 100, 1)
    p2 = Product("Товар2", "Описание", 200, 1)
    category = Category("Категория", "Описание", [p1, p2])

    result = [product for product in category]

    assert result == [p1, p2]


def test_order_create():
    product = Product("Товар", "Описание", 100, 5)
    order = Order(product, 3)

    assert order.product is product
    assert order.quantity == 3


def test_order_total_price():
    product = Product("Товар", "Описание", 100, 5)
    order = Order(product, 3)

    assert order.total_price == 300


def test_order_wrong_product():
    with pytest.raises(TypeError):
        Order("не продукт", 1)