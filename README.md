# Transactions Project

Проект для анализа транзакций, генерации отчетов и демонстрации работы с продуктами и категориями.

## Структура проекта
transactions_project/
├── src
│   ├── init.py
│   ├── utils.py
│   ├── reports.py
│   ├── main.py
│   ├── models.py
│   ├── views.py
│   └── services.py
├── tests
│   ├── init.py
│   └── test_reports.py
├── README.md
└── pyproject.toml

## Установка и зависимости

Используется Poetry:

bash
poetry install

Зависимости:
 • pandas – работа с таблицами
 • openpyxl – чтение/запись Excel
 • pytest – тестирование
 • black – автоформатирование
 • isort – сортировка импортов
 • flake8 – проверка стиля кода

Использование

## Загрузка данных из Excel

from src.utils import load_transactions

df = load_transactions("data/operations.xlsx") 

## Генерация отчетов

from src.reports import spending_by_category, spending_by_weekday, spending_by_workday

report1 = spending_by_category(df, "Фастфуд")
report2 = spending_by_weekday(df)
report3 = spending_by_workday(df)

## Работа с продуктами и категориями

from src.models import Product, Category

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
category1 = Category("Смартфоны", "Описание категории", [product1])

print(category1.name)
print(category1.products)

## Тестирование

pytest

## Форматирование кода
 • Black: black src tests
 • isort: isort src tests
 • Flake8: flake8 src tests

## Особенности
 • Разделение бизнес-логики и работы с данными
 • Декоратор для отчетов с автоименем файла
 • Подготовка к расширению: сервисы, API, веб-интерфейс
 • Совместимо с Python 3.10+
 
# Магазин товаров (OOP)

Проект реализует систему управления товарами магазина
с использованием объектно-ориентированного программирования.

## Реализованный функционал

### Продукты
- Базовый класс Product:
  - название
  - описание
  - цена (приватный атрибут)
  - количество
  - поддержка сложения товаров одного типа

### Категории продуктов
- Класс Category
- Добавление только продуктов или их наследников
- Защита от добавления посторонних объектов

### Наследники Product
- Smartphone
  - производительность
  - модель
  - объем памяти
  - цвет

- LawnGrass
  - страна-производитель
  - срок прорастания
  - цвет

### Ограничения
- Нельзя складывать товары разных типов (`TypeError`)
- В категорию нельзя добавить объект,
  не являющийся продуктом или его наследником

## Тестирование
- Используется pytest
- Все тесты проходят без ошибок