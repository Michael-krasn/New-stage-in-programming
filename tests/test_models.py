import pytest
from src.models import Product, Category


def test_add_product_and_get_products():
    # Создаем продукты
    p1 = Product("Товар1", "Описание1", 100, 5)
    p2 = Product("Товар2", "Описание2", 200, 10)

    # Создаем категорию без продуктов
    category = Category("Категория1", "Описание категории")

    # Добавляем первый продукт
    category.add_product(p1)

    products_str = category.products
    assert "Товар1, 100 руб. Остаток: 5 шт." in products_str
    assert category.product_count == 1

    # Добавляем второй продукт
    category.add_product(p2)

    products_str = category.products
    assert "Товар2, 200 руб. Остаток: 10 шт." in products_str
    assert category.product_count == 2


def test_new_product_classmethod():
    data = {"name": "Товар3", "description": "Описание3", "price": 300, "quantity": 7}
    product = Product.new_product(data)

    assert product.name == "Товар3"
    assert product.description == "Описание3"
    assert product.price == 300
    assert product.quantity == 7


def test_price_setter_and_getter(capsys):
    product = Product("Товар4", "Описание4", 150, 3)

    # Проверяем текущую цену
    assert product.price == 150

    # Меняем цену на положительное число
    product.price = 200
    assert product.price == 200

    # Меняем цену на отрицательное число, должна быть ошибка в консоли
    product.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    # Цена не изменилась
    assert product.price == 200

    # Меняем цену на 0
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 200
