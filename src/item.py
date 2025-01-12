import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path='src/items.csv'):
        try:
            with open(path, 'r', encoding='windows-1251') as csvfile:
                dict_ = csv.DictReader(csvfile, delimiter=',')
                cls.all.clear()
                for row in dict_:
                    if len(row) != 3:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    cls(row['name'], Item.string_to_number(row['price']), Item.string_to_number(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('.')
        return self.quantity + other.quantity

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'


class InstantiateCSVError(Exception):
    """Файл item.csv поврежден"""
    pass
