class Product:
    def __init__(self, name, description, price, quantity=0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    # алиас для автотестов
    def init(self, *args, **kwargs):
        self.__init__(*args, **kwargs)

    @classmethod
    def new_product(cls, data):
        return cls(
            data["name"],
            data["description"],
            data["price"],
            data.get("quantity", 0),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        efficiency,
        model,
        memory,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return self.quantity + other.quantity


class LawnGrass(Product):
    def __init__(
        self,
        name,
        description,
        price,
        quantity,
        country,
        germination_period,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return self.quantity + other.quantity


class Category:
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

    def init(self, *args, **kwargs):
        self.__init__(*args, **kwargs)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.products.append(product)
        Category.product_count += product.quantity

    def __str__(self):
        total = sum(p.quantity for p in self.products)
        return f"{self.name}, количество продуктов: {total} шт."

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
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.category.products):
            raise StopIteration
        product = self.category.products[self.index]
        self.index += 1
        return product