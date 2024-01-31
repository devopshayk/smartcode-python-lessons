# color = input("Enter the color of the phone: ").lower()
# model = input("Enter the model of the phone: ").lower()

# gold_iphone_12 = (color == "gold") and (model == "iphone 12")

# buy_phone = gold_iphone_12

# print("You are buying the gold iPhone 12." * buy_phone)

# --------------> task 1



# answer1 = input("Question 1: What is the capital of France? ").lower()
# answer2 = input("Question 2: What is 2 + 2? ")
# answer3 = input("Question 3: What is the chemical symbol for water? ").lower()
# answer4 = input("Question 4: What is the largest mammal? ").lower()
# answer5 = input("Question 5: What year did World War II end? ")

# is_correct = (answer1 == "paris") and \
#              (answer2 == "4") and \
#              (answer3 == "h2o" or answer3 == "water") and \
#              (answer4 == "blue whale") and \
#              (answer5 == "1945")

# print(is_correct)

# --------------> task 2



# age = int(input("Enter employee's age: "))
# experience = float(input("Enter employee's years of experience: "))

# min_age = 17
# max_age = 25
# min_experience = 2.0

# is_hired = (min_age <= age <= max_age) * (experience >= min_experience)

# print("Employee meets the requirements and is hired:" * is_hired)

# --------------> task 3



# dream_car = "Tesla Model S"

# car_data = "Toyota Camry, Honda Civic, Tesla Model S, Ford Mustang, BMW X5"

# buy_dream_car = dream_car in car_data

# print("You can buy your dream car:", buy_dream_car)

# --------------> task 4



# a = 5
# b = 6

# result = a**3 + 3 * a**2 * b + 3 * a * b**2 + b**3

# print("(a + b)^3 =", result)

# --------------> task 5



# import random

# numbers_str = "1 3 5 7 9"

# numbers = [int(num) for num in numbers_str.split()]

# random_number = random.randint(1, 10)

# found = random_number in numbers

# print("Random number generated:", random_number)
# print("Found in the list:", found)

# --------------> task 6



# num = int(input("Enter a number: "))

# factorial = 1

# factorial *= (num >= 1) * num
# factorial *= (num >= 2) * (num - 1)
# factorial *= (num >= 3) * (num - 2)
# factorial *= (num >= 4) * (num - 3)
# factorial *= (num >= 5) * (num - 4)

# print("The factorial of", num, "is:", factorial)

# --------------> task 7



# grams = int(input("Enter the grams of tobacco: "))

# cigarettes = grams // 20

# print("The number of cigarettes is:", cigarettes)

# --------------> task 8