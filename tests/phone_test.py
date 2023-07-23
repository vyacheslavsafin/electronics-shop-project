from src.item import Item
from src.phone import Phone
import pytest


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    assert phone.__str__() == 'iPhone 14'

def test_number_of_sim(phone):
    assert phone.number_of_sim == 2

def test_number_of_sim_setter(phone):
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
