import pytest
from src.item import Item
from src.phone import Phone

@pytest.fixture
def fixt():
    Item.pay_rate = 0.8
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def phone1():
    return Item("iPhone 14", 120_000, 5)

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)
