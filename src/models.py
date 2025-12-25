class Product:
    def __init__(self, name, *args):
        self.name = name
        if len(args) == 2:
            self.description = None
            self.__price = args[0]
            self.quantity = args[1]
        elif len(args) == 3:
            self.description = args[0]
            self.__price = args[1]
            self.quantity = args[2]
        else:
            self.description = None
            self.__price = 0
            self.quantity = 0

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            data["name"],
            data.get("description"),
            data["price"],
            data["quantity"],
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    @property
    def product_count(self):
        return sum(product.quantity for product in self.products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index >= len(self.products):
            raise StopIteration
        product = self.products[self._index]
        self._index += 1
        return product


class CategoryIterator:
    def __init__(self, category):
        self._products = category.products
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._products):
            raise StopIteration
        product = self._products[self._index]
        self._index += 1
        return product