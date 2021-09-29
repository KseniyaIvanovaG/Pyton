from itertools import cycle
from time import sleep

class TrafficLight:
    colors_queue = ("красный", "желтый", "зеленый")
    time_queue = (7, 2, 8)
    message = ("Красный", "Желтый", "Зеленый")

    def __init__(self, color):
        self.__color = color

    def running(self):
        my_cycle = cycle(self.colors_queue)
        for traffic_color in my_cycle:
            if self.__color == traffic_color:
                print(self.message[self.colors_queue.index(self.__color)])
                sleep(self.time_queue[self.colors_queue.index(self.__color)])
                self.__color = next(my_cycle)

my_traffic = TrafficLight("красный")
my_traffic.running()


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length
    def get_weight_of_asphalt(self, weight_ratio, thikness):
        asphalt = self._length * self._width * weight_ratio * thikness
        return asphalt
my_road = Road(20, 5000)
print(my_road.get_weight_of_asphalt(25, 0.5))


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']
my_position = Position('Tom', 'Cruise', 'actor', '8500000000', '2')
print(f'Total salary of {my_position.get_full_name()} is {my_position.get_full_salary()}')


class Cars:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print("Привет!")
    def go(self):
        print(f"Машина {self.color} цвета, марки {self.name} поехала со скоростью {self.speed}")
    def stop(self):
        print(f"Машина {self.color} цвета, марки {self.name} остановилась")
    def turn(self):
        print(f"Машина {self.color} цвета, марки {self.name} повернула на{direction}")
    def show_speed(self):
        print(f"Текущая скорость машины {self.speed}")

class TownCar(Cars):
    def __init__(self, speed, color, name, is_police):
        Cars.__init__(self, speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else:
            Cars.show_speed(self)
class SportCar(Cars):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police=False)
class WorkCar(Cars):
    def __init__(self, speed, color, name, is_police):
        Cars.__init__(self, speed, color, name, is_police=False)
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
class PoliceCar(Cars):
    def __init__(self, speed, color, name, is_police):
        Cars.__init__(self, speed, color, name, is_police=True)

my_police_car = PoliceCar(90, "blue", "Tesla", True)
my_police_car.go()
my_police_car.turn("лево")
my_police_car.stop()
my_police_car.show_speed()

my_work_car = WorkCar(50, "orange", False)
my_work_car.go()
my_work_car.turn("лево")
my_work_car.stop()
my_work_car.show_speed()

my_sport_car = SportCar(200, "black", "BMW")
my_sport_car.go()
my_sport_car.turn("право")
my_sport_car.stop()
my_sport_car.show_speed()

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print(f'We are drawing by {self.title}')

class Pencil(Stationary):
    def draw(self):
        print(f'We are drawind by {self.title}')

class Handle(Stationary):
    def draw(self):
        print(f'We are drawing by {self.title}')

pen = Pen("pen")
pencil = Pencil("pencil")
handle = Handle("handle")
pen.draw()
pencil.draw()
handle.draw()

