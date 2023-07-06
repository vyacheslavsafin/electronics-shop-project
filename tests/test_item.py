"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.calculate_total_price()
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)

    item1.apply_discount()
    assert item1.price == 8000.0

def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('3') == 3

def test_repr(fixt):
    assert fixt.__repr__() == "Item('Смартфон', 10000, 20)"

def test_str(fixt):
    assert fixt.__str__() == 'Смартфон'

def test_setter_name(fixt):
    fixt.name = 'name'
    assert fixt.name == 'name'
    fixt.name = 'verylongname'
    assert fixt.name == 'verylongna'
