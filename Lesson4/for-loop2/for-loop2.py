# for num in range(10, 100):
#     first_digit = num // 10
#     second_digit = num % 10
#     triple_product = (first_digit * second_digit) * 3
#     if triple_product == num:
#         print(num)
        
# --------------> task 1



# grechka_supply = 100  
# monthly_consumption = 4  

# for month in range(1, 25):  
#     print(f"Month {month}: {grechka_supply} kg grechka")
#     grechka_supply -= monthly_consumption  

    
#     if grechka_supply <= 0:
#         print("Grechka is over.")
#         break

# --------------> task 2



# letter_width = float(input("Enter the width of the letter in centimeters: "))
# letter_height = float(input("Enter the height of the letter in centimeters: "))

# num_folds = 0

# while letter_width > 12 or letter_height > 12:
#     letter_width /= 2
#     letter_height /= 2
    
#     num_folds += 1

# print("To fit the letter into the envelope, you need to fold it in half", num_folds, "times.")

# --------------> task 3



# educational_grant = float(input("Enter the educational grant amount in rubles: "))  
# expenses = float(input("Enter the initial monthly living expenses in rubles: "))  
# months = 10  
# increase_rate = 0.03 

# total_expenses = expenses
# for month in range(2, months + 1):
#     expenses *= (1 + increase_rate)  
#     total_expenses += expenses

# required_amount = total_expenses - educational_grant * months

# print("The total amount needed from parents at the beginning of the education:", required_amount, "rubles")

# --------------> task 4



# count = 0

# for i in range(10):
#     word = input("Введите слово: ")
#     if word.lower() == "карамба":  
#         count += 1

# print("Количество введенных слов, совпадающих со словом 'Карамба':", count)

# --------------> task 5