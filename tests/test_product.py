import pytest
from src.models import Product

def test_product_zero_quantity_raises_value_error():
    with pytest.raises(ValueError) as exc:
        Product("ТестТовар", "Описание", 100, 0)
    assert str(exc.value) == "Товар с нулевым количеством не может быть добавлен"
