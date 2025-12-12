# tests/test_main.py

import pytest
from src.main import Product, Category

@pytest.fixture
def sample_products():
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [p1, p2, p3]

@pytest.fixture
def sample_category(sample_products):
    # Сбрасываем счетчики перед созданием
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Категория смартфонов", sample_products)

def test_product_initialization(sample_products):
    p1 = sample_products[0]
    assert p1.name == "Samsung Galaxy S23 Ultra"
    assert p1.description == "256GB, Серый цвет, 200MP камера"
    assert p1.price == 180000.0
    assert p1.quantity == 5

def test_category_initialization(sample_category, sample_products):
    c = sample_category
    assert c.name == "Смартфоны"
    assert c.description == "Категория смартфонов"
    assert len(c.products) == 3
    assert c.products == sample_products

def test_category_count(sample_category):
    c2 = Category("Телевизоры", "Категория телевизоров", [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])
    assert Category.category_count == 2  # 2 категории созданы
    assert c2.category_count == 2        # у объекта тоже корректно

def test_product_count(sample_category):
    c2 = Category("Телевизоры", "Категория телевизоров", [Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)])
    assert Category.product_count == 4  # 3+1 продукта всего
    assert sample_category.product_count == 3  # у первой категории своё количество
