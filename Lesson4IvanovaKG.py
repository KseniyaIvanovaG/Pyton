
from sys import argv

script_name, productivity, rate_per_hour, bonus = argv
print('Name of script: ', script_name)
print('Productivity, hours: ', productivity)
print('Rate per hour: ', rate_per_hour)
print('Bonus: ', bonus)
print('Salary: ', int(productivity) * int(rate_per_hour) + int(bonus))


def my_def():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f'Исходный список: {my_list}')
    final_list = [my_list[index] for index in range(1, len(my_list)) if my_list[index] > my_list[index-1]]
    print(f'Результат: {final_list}')

if __name__ == "__main__":
    my_def()


result = [element for element in range(20, 241) if element % 20 == 0 or element % 21 == 0]
print(result)


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список: ', my_list)

final_list = [el for el in my_list if my_list.count(el) == 1]
print('Результат: ', final_list)


from functools import reduce
my_list = [el for el in range(100, 1001, 2)]
print(my_list)
result = reduce(lambda x, y: x*y, my_list)
print(result)


from itertools import count, cycle
import sys

start_from = 10
iterable = 'ABCDEF'
iterations_count = 0

def integer_generator(start_from):
    for el in count(start_from):
        if el > start_from+10:
            break
        yield el

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break


from itertools import count
def fact(n):
    result = 1
    for i in count(1):
        if i <= n:
            result *= 1
            yield result
        else:
            break

for el in fact(1000):
    print(el)


