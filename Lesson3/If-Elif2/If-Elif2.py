# experience_points = int(input("Your opit: "))

# level = 1

# if experience_points >= 5000:
#     level = 4
# elif experience_points >= 2500:
#     level = 3
# elif experience_points >= 1000:
#     level = 2

# print("Your level:", level)

# --------------> task 1



# place = int(input("Enter the student's place in the applicant list: "))
# points = int(input("Enter the exam score: "))

# if place <= 10:
#     print("Congratulations, you have been accepted!")
    
#     if points >= 290:
#         print("You will be awarded a scholarship as a bonus.")
#     else:
#         print("But you did not score enough points for a scholarship.")
# else:
#     print("Unfortunately, you were not accepted.")

# --------------> task 2



# numbers = input("Enter three numbers separated by space: ")

# num1, num2, num3 = map(int, numbers.split())

# if num1 == num2 == num3:
#     print(3)
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print(2)
# else:
#     print(0)

# --------------> task 3



# price = float(input("Enter the price of the apartment in million rubles: "))
# area = float(input("Enter the area of the apartment in square meters: "))

# if (area >= 100 and price <= 10) or (area >= 80 and price <= 7):
#     print("The apartment fits!")
# else:
#     print("The apartment doesn't fit.")

# --------------> task 4



# hour = int(input("Enter the hour (from 0 to 23): "))

# if (hour < 8 or (hour >= 10 and hour < 12) or (hour >= 14 and hour < 15) or (hour >= 18 and hour < 20) or hour >= 22):
#     print("You cannot receive a package")
# else:
#     print("You can receive a package")
    
# --------------> task 5



# dog_age = float(input("Enter the dog's age in dog years: "))

# if dog_age <= 2:
#     human_age = dog_age * 10.5
# else:
#     human_age = 21 + (dog_age - 2) * 4

# print("The dog's age in human years is:", human_age)

# --------------> task 6