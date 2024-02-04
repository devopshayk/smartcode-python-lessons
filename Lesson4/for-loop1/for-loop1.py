# for i in range(1, 1000):
#     if i % 25 == 0 and i % 15 == 0:
#         break
# print(f'The smallest is {i}')

# --------------> task 1



# odd_num = 0
# even_num = 0

# for i in range(1, 101):
#     if i % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1
        
# print(f'Odd nums is {odd_num}, and even nums is {even_num}')   

# --------------> task 2   



# string = 'python 3.9'
# nums = 0
# text = 0

# for i in string:
#     if i.isdigit():
#         nums += 1
#     elif i.isalpha():
#         text += 1

# print(f'Num is {nums}, and text is {text}')        

# --------------> task 3



# number = 73421
# number_str = str(number)  
# total = 0

# for char in number_str:
#     digit = int(char)  
#     total += digit  

# print("Sum of digits in", number, "is:", total)

# --------------> task 4



# number = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print("The factorial of", number, "is:", factorial)

# --------------> task 5



# count = 0  

# for i in range(10):
#     number = int(input(f"Number  {i+1}: "))
#     if number > 0 and number % 2 == 0:  
#         count += 1

# print("Out of the entered numbers", count, " are simultaneously even and positive.")

# --------------> task 6



# total_salary = 0

# for month in range(1, 13):
#     salary = float(input(f"Enter the salary for month {month}: "))
#     total_salary += salary  

# average_salary = total_salary / 12

# print("The average salary for the year is:", average_salary)

# --------------> task 7