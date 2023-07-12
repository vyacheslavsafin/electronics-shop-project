from src.item import Item
from src.phone import Phone
import pytest


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone1):
    assert phone1.__str__() == 'iPhone 14'

