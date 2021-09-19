def my_result(a=int(input()), b=int(input())):
    if b == 0:
        print("деление на ноль невозможно")
    else:
        return a / b
print(my_result())


def identification(**kwargs):
    return f"имя:{kwargs['name']}. фамилия:{kwargs['surname']}, год рождения:{kwargs['year']}, город: {kwargs['city']}, " \
           f"почта:{kwargs['email']}, телефон:{kwargs['phone']}"
print(identification(name="Kseniya", surname="Ivanova", year="1989", city="Khimki", email="k@m.ru", phone="677-69-76"))


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort(reverse=True)
    return sum(my_list[:2])
print(my_func(1,2,3))

# вопрос к преподавателю: я посмотрела разбор д/з, почему нельзя было таким способом решить заадчу?:
def my_func(x, y):
    return x**y
print(my_func(2, -7))

def sum_calc(input_string):
    input_list = input_string.split()
    my_sum = 0
    for el in input_list:
        if el:
            try:
                if el =="N":
                    return my_sum, False
                else:
                    my_sum +=float(el)
            except ValueError:
                continue
    return my_sum, True
continue_flag = True
result_sum = 0
while continue_flag:
    input_string = input("Введите числа через пробел. Для остановки введите N: ")
    current_sum, continue_flag = sum_calc(input_string)
    result_sum +=current_sum
    print("Промежуточная сумма: ", result_sum)
print("Результирующая сумма: ", result_sum)


int_func = lambda word: word.capitalize()
input_string = input("Введите строку: ")
result_string_list = []
input_words = input_string.split()
for element in input_words:
    result_string_list.append(int_func(element))
print(" ".join(result_string_list))





