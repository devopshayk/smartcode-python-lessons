# def find_max(num1, num2):
    
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# maximum = find_max(num1, num2)

# print("The maximum of the two numbers is:", maximum)

# --------------> task 1



# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     return x / y

# print("Select operation:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# while True:
#     choice = input("Enter choice (1/2/3/4): ")

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#     else:
#         print("Invalid input")


# --------------> task 2



# def sum_all_numbers():
#     total = 0
#     num = float(input("Enter a number (enter 0 to terminate): "))
    
#     while num != 0:
#         total += num
#         num = float(input("Enter a number (enter 0 to terminate): "))

#     print("The sum of all numbers entered is:", total)

# sum_all_numbers()

# --------------> task 3



# def multiply_all_numbers():
#     product = 1
#     num = float(input("Enter a number (enter 1 to terminate): "))
    
#     while num != 1:
#         product *= num
#         num = float(input("Enter a number (enter 1 to terminate): "))

#     print("The product of all numbers entered is:", product)

# multiply_all_numbers()

# --------------> task 4



# passenger_ages = []

# for i in range(3):
#     age = int(input("Enter passenger's age: "))
#     passenger_ages.append(age)

# for age in passenger_ages:
#     if age < 16:
#         print("Too young!")
#         break
# else:
#     print("Get ready!")
    
# --------------> task 5