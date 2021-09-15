my_list = ['a', 8, 5, 'лето', (1, 2, 3)]
for i in my_list:
      print(type(i))


some_list = input()
my_list = list(some_list)
for el in range(0, len(my_list) - 1, 2):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print(my_list)

month = int(input())
year_dict = {}
year_dict = year_dict.fromkeys([12, 1, 2], "Зима")
year_dict.update({}.fromkeys([3, 4, 5], "Весна"))
year_dict.update({}.fromkeys([6, 7, 8], "Лето"))
year_dict.update({}.fromkeys([9, 10, 11], "Осень"))
print(year_dict.get(month))


month = int(input())
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print("Зима")
elif month in spring:
    print("Весна")
elif month in summer:
    print("Лето")
elif month in autumn:
    print("Осень")
else:
    print("Месяц введен неправильно")


string = input("Введите нескольких слов, разделённых пробелами:")
string_1 = (string.split(" "))
for i, word in enumerate(string_1):
    print(i, word[:10])


my_list = [7, 5, 3, 3, 2]
rating_element = int(input("Введите новый элемент рейтинга"))
if rating_element < my_list[-1]:
    my_list = my_list.append(rating_element)
elif rating_element > my_list[0]:
    my_list = my_list.insert(0, rating_element)
else:
    for rating in my_list:
        if rating == rating_element:
            rating_index = my_list.index(rating)
            rating_count = my_list.count(rating)
            new_index = rating_index + rating_count
            my_list.insert(new_index, rating_element)
            break
        elif rating_element > rating:
            my_list.insert(my_list.index(rating), rating_element)
            break
        else:
            continue
print(my_list)


