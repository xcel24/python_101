# birth_year = input("What is your birth year? ")
# name = input("What is your name? ")
# age = 2024 - int(birth_year)
#
# print("your name and age is", name, age)

course = "Python for beginners"
# print(course[:])
#
# first_name = "Prateek"
# last_name = "Goswami"
#
# msg = f"{first_name} [{last_name}] is a coder"
#
# print(msg)

#String functions
# len()
# course.upper()
# course.lower()
# course.find()
# course.replace()
# "Python" in course

#Math Functions

# import math
#
# x = 5
# y = 10
# print(math.factorial(5))
# print(math.log(y,10))

# is_hot_day = True
# is_cold_day = False
#
# if is_hot_day:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold_day:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# i = 1
# while i <= 5:
#     print(f"value of i is {i}")
#     i += 1

# ans = 9
#
# n = input("Guess: ")
# cnt = 1
#
# while cnt <= 3:
#     if int(n) == ans:
#         print("You guessed correctly")
#         break
#     else:
#         n = input("Guess: ")
#     cnt += 1
#
# if cnt > 3:
#     print("Game Over :(")

# For loops
# for item in "Python":
#     print(item)
#
# for item in ["Prateek","Goswami","IIT","Kharagpur"]:
#     print(item)

# for item in range(1, 10, 5):
#     print(item)

# for x in range(3):
#     for y in range(3):
#         print(f"({x},{y})")

# temp = [5, 2, 5, 2, 2]
#
# for patt in temp:
#     print("*" * patt)

numbers = [3, 6, 2, 18, 4, 10]

max_value = numbers[0]

for num in numbers[1:]:
    if num > max_value:
        max_value = num

print(max_value)


