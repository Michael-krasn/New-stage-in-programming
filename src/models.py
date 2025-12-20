class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # ✅ приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

class Category:
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category._category_count += 1
        Category._product_count += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category._product_count += 1

    @property
    def products(self):
        return "\n".join(
            [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
        )

    @property
    def category_count(self):
        return Category._category_count

    @property
    def product_count(self):
        return len(self.__products)