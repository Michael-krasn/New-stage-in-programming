import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_add_product_and_get_products():
    p1 = Product("Товар1", "Описание1", 100, 5)
    p2 = Product("Товар2", "Описание2", 200, 10)

    category = Category("Категория1", "Описание категории")

    category.add_product(p1)
    assert str(p1) in [str(p) for p in category.products]
    assert category.product_count == 5

    category.add_product(p2)
    assert str(p2) in [str(p) for p in category.products]
    assert category.product_count == 15


def test_new_product_classmethod():
    data = {
        "name": "Товар3",
        "description": "Описание3",
        "price": 300,
        "quantity": 7,
    }

    product = Product.new_product(data)

    assert product.name == "Товар3"
    assert product.description == "Описание3"
    assert product.price == 300
    assert product.quantity == 7


def test_price_setter_and_getter(capsys):
    product = Product("Товар4", "Описание4", 150, 3)

    assert product.price == 150

    product.price = 200
    assert product.price == 200

    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 200

    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 200


def test_product_str():
    product = Product("Телефон", 80, 15)
    assert str(product) == "Телефон, 80 руб. Остаток: 15 шт."


def test_category_str():
    product1 = Product("Телефон", 80, 10)
    product2 = Product("Наушники", 20, 5)

    category = Category("Электроника", "Описание", [product1, product2])

    assert str(category) == "Электроника, количество продуктов: 15 шт."


def test_product_add():
    a = Product("A", 100, 10)
    b = Product("B", 200, 2)

    assert a + b == 1400


def test_price_getter():
    product = Product("Товар", 100, 1)
    assert product.price == 100


def test_category_iterator():
    product1 = Product("Телефон", 80, 10)
    product2 = Product("Наушники", 20, 5)

    category = Category("Электроника", "Описание", [product1, product2])

    products = [product.name for product in category]
    assert products == ["Телефон", "Наушники"]


def test_category_iterator_class():
    product1 = Product("Телефон", 80, 10)
    product2 = Product("Наушники", 20, 5)

    category = Category("Электроника", "Описание", [product1, product2])

    products = []
    for product in CategoryIterator(category):
        products.append(product.name)

    assert products == ["Телефон", "Наушники"]


def test_smartphone_creation():
    phone = Smartphone(
        "iPhone",
        "Apple smartphone",
        100000,
        5,
        efficiency=95,
        model="15 Pro",
        memory=256,
        color="black",
    )

    assert phone.name == "iPhone"
    assert phone.model == "15 Pro"
    assert phone.memory == 256
    assert phone.color == "black"
    assert phone.price == 100000


def test_lawn_grass_creation():
    grass = LawnGrass(
        "Газон",
        "Зелёный газон",
        500,
        20,
        country="Россия",
        germination_period=14,
        color="green",
    )

    assert grass.country == "Россия"
    assert grass.germination_period == 14
    assert grass.color == "green"


def test_add_same_product_types():
    phone1 = Smartphone("A", "desc", 10, 3, 90, "X", 128, "black")
    phone2 = Smartphone("B", "desc", 10, 2, 90, "Y", 256, "white")

    assert phone1 + phone2 == 5


def test_add_different_product_types():
    phone = Smartphone("A", "desc", 10, 3, 90, "X", 128, "black")
    grass = LawnGrass("B", "desc", 5, 10, "Россия", 7, "green")

    with pytest.raises(TypeError):
        phone + grass


def test_add_product_to_category():
    category = Category("Товары", "Описание")
    product = Product("Товар", "Описание", 100, 1)

    category.add_product(product)
    assert len(category.products) == 1


def test_add_not_product_to_category():
    category = Category("Товары", "Описание")

    with pytest.raises(TypeError):
        category.add_product("не продукт")
