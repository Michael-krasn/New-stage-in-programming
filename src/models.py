from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LoggerMixin:
    def __init__(self, *args, **kwargs):
        cls_name = self.__class__.__name__
        print(
            f"[LOG] Создан объект класса {cls_name} с параметрами: args={args}, kwargs={kwargs}"
        )
        super().__init__(*args, **kwargs)


class Product(LoggerMixin, BaseProduct):
    def __init__(self, name, description, price, quantity=0):
        self.__price = None
        super().__init__(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price = value

    def add(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только товары одного типа")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def add(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только смартфоны")
        return self.quantity + other.quantity

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def add(self, other):
        if type(self) is not type(other):
            raise TypeError("Можно складывать только газонную траву")
        return self.quantity + other.quantity

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных типов")
        return self.price * self.quantity + other.price * other.quantity


class CountableItem(ABC):
    category_count = 0
    product_count = 0

    @abstractmethod
    def total_price(self):
        pass


class Category(CountableItem):
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in self.products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
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

    def total_price(self):
        return sum(p.price * p.quantity for p in self.products)


class Order(CountableItem):
    def __init__(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("В заказе должен быть Product")
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return (
            f"Заказ: {self.product.name}, "
            f"Количество: {self.quantity}, "
            f"Итоговая цена: {self.total_price} руб."
        )
