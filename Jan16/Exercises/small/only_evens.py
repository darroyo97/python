# numbers = [1, 2, 3, 4, 5]

number = 5
list_of_num = [0, 1, 2, 3, 4]


def even_check(number):
    if (number % 2) == 0:
        print(number)


even_check(number)


def only_even(list_of_num):
    for number in list_of_num:
        if even_check(number):
            return only_even(list_of_num)


only_even(list_of_num)
# even_list = [evens]
# print(even_list)

# def only_evens(numbers):
#     even_list = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_list.append(num)
#             print(even_list)

# only_evens(numbers)
