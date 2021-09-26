input_str = input('Введите следующую строку: ')
with open("File", "a") as file:
    while input_str:
        file.write(input_str+'\n')
        input_str = input('Введите следующую строку:')


with open("File") as file:
    file_lines = file.readlines()
    print("Количество строк в файле: ", len(file_lines))
    for line_number, line in enumerate(file_lines, 1):
        print(f"Количество слов в строке {line_number}:", len(line.split()))



sum = 0
with open("task3") as file:
    lines = file.readlines()
    for line in lines:
        surname, salary = line.split()
        sum += int(salary)
        if int(salary) < 20000:
            print("Имеет оклад менее 20 тысяч: ", surname)
print("Средняя величина дохода:", sum/len(lines))


translate_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("task4") as file_read, open("task4translate", "w") as file_write:
    for line in file_read.readlines():
        text_number, number = line.rstrip().split(' — ')
        file_write.write(f'{translate_dict[text_number]} - {number}\n')


with open("task5", "w") as file_w:
    input_numbers = input("Введите числа через пробел: ")
    print(input_numbers, file=file_w)

with open("task5") as file:
    content_list = file.read().rstrip().split()
    print(content_list)
    numbers_list = [int(number) for number in content_list if number.isdigit()]
    print(numbers_list)
    print(sum(numbers_list))


result_dict = {}
with open("task6") as file:
    for line in file:
        lesson_type, *lessons = line.split()
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '—']
        result_dict.update({lesson_type.rstrip(":"): sum(lesson_count)})
print(result_dict)


import json
result_list = []
dict_plus_profit = {}
dict_minus_profit = {}
with open("task7") as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update({name: profit})
        else:
            dict_minus_profit.update({name, profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_minus_profit)
    result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})
with open("task7.json", "w") as file:
    json.dump(result_list, file)