import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard

@pytest.fixture
def fixt():
    Item.pay_rate = 0.8
    return Item("Смартфон", 10000, 20)

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)
