print("Hello, world")
today_weather = 'Сегодня отличная погода'
print(today_weather)
action = 'Самое время погулять'
print(action)


name = str(input('Привет! Введи своё имя'))
print('Хорошего тебе дня,%s' % name)
mood = str(input("Как настроение?"))
city = str(input("В каком городе ты живешь?"))
temperature = str(input ("Какая температура сейчас на улице?"))
print ("Знакомьтесь, это %s" % name)
print("У%s" % name, "сегодня%s" % mood, "настроение")
print(name,"живет в городе%s" % city, "и в этом городе сейчас%s" % temperature,"градусов.")


seconds_user = int (input('Введите время в секундах'))
hours = seconds_user // 3600
minutes = seconds_user % 3600 // 60
seconds = seconds_user % 3600 % 60
print(f"{hours:02d} : {minutes:02d} : {seconds:02d}")

number = input ("Введите число")
number_2 = number + number
number_3 = number + number + number
sum_number = int (int(number) + int(number_2) + int(number_3))
print(sum_number)


num = input("Введите целое положительное число")
num_length = len(num)
max_element = 0
i = 0
while i < num_length:
    current_element = int(num[i])
    if current_element > max_element:
         max_element = current_element
        i += 1
print(max_element)

earnings = int(input("Введите значение выручки"))
costs = int(input("Введите значение издержек"))
profit = earnings - costs
if earnings > costs:
    print("Компания работает с прибылью")
if earnings < costs:
    print("Компания работает с убытком")
if earnings > costs:
    profitability = profit / earnings
    number_of_staf = int(input("Введите численность сотрудников"))
    profit_to_staf = profit / number_of_staf
    print("Прибыль фирмы в расчёте на одного сотрудника: %s"% profit_to_staf)


dayly_distance = int(input("Сколько километров спортсмен пробегает за день:"))
target_distance = int(input("Сколько километров нужно ему пробегать в день:"))
days = 1
while dayly_distance < target_distance:
    dayly_distance *= 1.1
    days += 1
print(f"На {days} день спортсмен будет бежать {target_distance} километров")
