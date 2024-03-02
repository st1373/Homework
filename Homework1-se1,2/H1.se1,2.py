##--Q1
# def count_letters(input_str):
#     uppercase_count = 0
#     lowercase_count = 0
#     for char in input_str:
#         if char.isupper():
#             uppercase_count += 1
#         elif char.islower():
#             lowercase_count += 1
#     print("Uppercase letters:", uppercase_count)
#     print("Lowercase letters:", lowercase_count)

# input_string = input("Enter a string: ")
# count_letters(input_string)
##--Q2
# def get_student_info(student_dict, name):
#     if name in student_dict:
#         print("Name:", name)
#         print("Major:", student_dict[name]['major'])
#         print("Age:", student_dict[name]['age'])
#     else:
#         print("Student not found.")
# # Dictionary
# students = {
#     'Samane': {'major': 'Computer Science', 'age': 20},
#     'Sanaz': {'major': 'Engineering', 'age': 22},
#     'Sara': {'major': 'Mathematics', 'age': 21}
# }
# input_name = input("Enter a name to search for: ")
# get_student_info(students, input_name)
##--Q3
# def count_odd_even(numbers):
#     numbers_tuple = tuple(numbers)
#     odd_count = 0
#     even_count = 0
#     for num in numbers_tuple:
#         if num % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     print(f"Odd numbers count: {odd_count}")
#     print(f"Even numbers count: {even_count}")
# numbers_list = [1,3,7,9,11,2,4,4,6,6,8,8,10]
# count_odd_even(numbers_list)
##Q4
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# user_input = int(input("Enter a number: "))
# if is_prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.")
