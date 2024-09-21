class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        """Метод вызывается перед созданием класса и
        возвращает ссылку на адрес в памяти, по которой будет создан
        новый экземпляр данного класса"""
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        """Инициализатор экземпляра класса"""
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        """Метод финализатор вызывается непосредственно перед удалением экземпляра класса"""
        print(f'{self.name} снесён, но он останется в истории')

    def go_to(self, new_floor: int):
        """Метод класса"""
        if 1 <= new_floor <= self.number_of_floors:
            for n in range(new_floor):
                print(n + 1)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        """Позволяет применять функцию len() к экземплярам класса"""
        return self.number_of_floors

    def __str__(self):
        """Применяется для отображения информации об объекте класса для пользователей,
        например для функций print, str."""
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    @classmethod
    def __verify_data__(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Операнд справа должен иметь тип int или House")
        return other if isinstance(other, int) else other.number_of_floors

    def __eq__(self, other):
        """Метод возвращает True, если два сравниваемых объекта равны между собой"""
        value = self.__verify_data__(other)
        return self.number_of_floors == value

    def __lt__(self, other):
        """Метод возвращает True, если первый объекта меньше второго объекта"""
        value = self.__verify_data__(other)
        return self.number_of_floors < value

    def __le__(self, other):
        """Метод возвращает True, если первый объекта меньше либо равен второму объекту"""
        value = self.__verify_data__(other)
        return self.number_of_floors <= value

    def __gt__(self, other):
        """Метод возвращает True, если первый объекта больше второго объекта"""
        value = self.__verify_data__(other)
        return self.number_of_floors > value

    def __ge__(self, other):
        """Метод возвращает True, если первый объекта больше либо равен второму объекту"""
        value = self.__verify_data__(other)
        return self.number_of_floors >= value

    def __ne__(self, other):
        """Метод возвращает True, если первый объекта не равен второму объекту"""
        value = self.__verify_data__(other)
        return self.number_of_floors != value

    def __add__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
        если 'value' принадлежит классу 'int'"""
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
                если 'value' принадлежит классу 'int'"""
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        """Метод увеличивает количество этажей на величину 'value',
                если 'value' принадлежит классу 'int'"""
        if isinstance(value, int):
            self.number_of_floors += value
            return self


#Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

