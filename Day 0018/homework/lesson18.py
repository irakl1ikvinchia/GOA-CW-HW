# N1

# def num_list(numbers):
#     result = []
#     for i in numbers:
#         if i % 4 == 0:
#             result.append(i)
#     return result

# new_list = []
# for i in range(20 + 1):
#     new_list.append(i)

# print(num_list(new_list))


# N2

# def user_info(name, surname):
#     user_list = []
#     user_name = input("Please enter your name: ")
#     user_surname = input("Please enter your surname: ")

#     user_list.append(user_name, user_surname)
#     return user_list

# print()


# N3

# def filter_list(start_num, end_num):
#     numbers = []
#     filtered_list = []

#     for i in range(start_num, end_num):
#         numbers.append(i)

#     for i in numbers:
#         if i % 2 == 0:
#             filtered_list.append(i ** 2)
#         else:
#             filtered_list.append(i ** 0.5)
#     return filtered_list

# start_num = int(input("enter start number: "))
# end_num = int(input("enter end number: "))

# result_list = filter_list(start_num, end_num)
# print(result_list)


# N4

# def sort_lastname(lastname):
#     char_list = []
#     even_index = []

#     for i in lastname:
#         char_list.append(i)

#     for index in range(len(char_list)):
#         if index % 2 == 0:
#             even_index.append(char_list[index])
#     return "".join(even_index)

# lastname = input("Please enter your lastname: ")
# print(sort_lastname(lastname))