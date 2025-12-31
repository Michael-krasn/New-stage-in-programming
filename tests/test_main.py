import pytest

from src.models import Category, LawnGrass, Smartphone


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )


@pytest.fixture
def smartphone3():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )


@pytest.fixture
def grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def grass2():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )


def test_smartphone_creation(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.memory == 256


def test_lawn_grass_creation(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.country == "Россия"
    assert grass1.price == 500.0


def test_smartphone_str_returns_string(smartphone1):
    result = str(smartphone1)
    assert isinstance(result, str)
    assert "Samsung" in result


def test_lawn_grass_str_returns_string(grass1):
    result = str(grass1)
    assert isinstance(result, str)
    assert "Газонная трава" in result


def test_add_smartphones(smartphone1, smartphone2):
    total = smartphone1 + smartphone2
    assert total == 180000.0 * 5 + 210000.0 * 8


def test_add_lawn_grass(grass1, grass2):
    total = grass1 + grass2
    assert total == 500.0 * 20 + 450.0 * 15


def test_add_different_product_types_raises_type_error(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_category_add_products(smartphone1, smartphone2, smartphone3):
    category = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
    )

    category.add_product(smartphone1)
    category.add_product(smartphone2)
    category.add_product(smartphone3)

    assert len(category.products) == 3
    assert smartphone1 in category.products


def test_category_add_not_product_raises_type_error():
    category = Category("Смартфоны", "Описание")

    with pytest.raises(TypeError):
        category.add_product("Not a product")
