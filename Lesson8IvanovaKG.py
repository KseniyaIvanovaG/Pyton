class Date:
    def __init__(self, date):
        self.date = date

    def extract_data(self):
        try:
            day, month, year = self.date.split("-")
            return int(day), int(month), int(year)
        except Exception as e:
            print(f"Не удалось выделить дату из строки {e}")

    @staticmethod
    def validate_data(date_input):
        try:
            day, month, year = date_input
            if day not in range(1,32):
                raise ValueError('День указан неверно')
            elif month not in range(1,13):
                raise ValueError('Месяц указан неверно')
            elif year not in range(0,2100):
                raise ValueError('Год указан неверно')
        except ValueError as e:
            print(e)
        else:
            print("Дата провалидирована успешно")

my_date_cls = Date('05-10-2021')
my_date = my_date_cls.extract_data()
print(my_date)
if my_date:
    my_date_cls.validate_data(my_date)


class ErrDivision(Exception):
    def __init__(self):
        self.txt = 'My division by zero'

def division(dividend, divisor):
    try:
        if divisor == 0:
            raise ErrDivision
        print(dividend / divisor)
    except ErrDivision as err:
        print(err.txt)
division(1,0)


class MyException(Exception):
    def __init__(self):
        self.txt = "Некорректный тип данных, необходимо ввести число"


mylist = []
input_string = input('Введите число, для выхода введите пустую строку')
while input_string:
    try:
        if input_string.isdigit():
            mylist.append(int(input_string))
        else:
            raise MyException
    except MyException as e:
        print(e.txt)

    input_string = input('Введите число, для выхода введите пустую строку')
print(mylist)


def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Недостаточно техники на складе!")
        except KeyError:
            print("Нет такого типа оргтехники на складе!")

    return wrapper


class Storage:
    """
    equipment_units имеет следующую структуру
    equipment_units = {
    "equipment_type": {
    "name": {
    "model": {
    "count": ""
    }
    }
    }
    }
    """
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]["count"] -= unit_count

    @staticmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Неверный формат входных данных!")
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model["count"] += self.__count
            else:
                equipment_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            equipment_storage_info[self.name] = {
                self.model: {"count": self.__count}
            }

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, "Printer", count)
        self.colors = colors


class Notebook(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, "Notebook", count)
        self.ram = ram
        self.system_type = system_type


my_printer_1 = Printer('Hp', 'XS5050', 2000, ['red', 'blue', 'green'])
my_printer_2 = Printer('Canon', 'TS304', 500, ['black'])
my_printer_3 = Printer('Xerox', 'B210', 1700, ['red', 'blue', 'green'])
my_printer_4 = Printer('Xerox', 'B210', 1300, ['red', 'blue', 'green'])
my_printer_5 = Printer('Xerox', 'B211', 200, ['red', 'blue', 'green'])

my_notebook_1 = Notebook("Lenovo", "ThinkPad X1", 2300, 8, "Windows")
my_notebook_2 = Notebook("Mac", "MacBookAir", 3200, 8, "MacOS")

# Storage.get_all_equipment()
Storage.storage_to(unit_type="Printer", unit_name="Hp", unit_model="XS5050", unit_count=100)
Storage.get_all_equipment()

Storage.storage_from(unit_type="Notebook", unit_name="Lenovo", unit_model="ThinkPad X1", unit_count=400)
Storage.get_all_equipment()


class Complex:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


my_complex_number_1 = Complex(9, 5)
my_complex_number_2 = Complex(-5, 6)
print(f"Сумма: {my_complex_number_1 + my_complex_number_2}")
print(f"Произведение: {my_complex_number_1 * my_complex_number_2}")

my_number_1 = complex(9, 5)
my_number_2 = complex(-5, 6)
print(my_number_1 + my_number_2)
print(my_number_1 * my_number_2)
