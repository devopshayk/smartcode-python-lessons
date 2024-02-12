# mixed_list = ["Hello", 42, 3.14, True, [1, 2, 3], {"name": "John", "age": 30}]

# --------------> task 1



# my_list = ["Hp", "Asus", "Dell", "Mac", "Lenovo"]

# has_mac = "Mac" in my_list

# print(has_mac)

# --------------> task 2




# password = "Python@$World11"


# if len(password) < 8:
#     print("Weak")
# else:
   
#     if sum(c.isdigit() for c in password) < 2:
#         print("Weak")
#     else:
       
#         special_characters = ('!', '@', '#', '$', '%', '&', '*')
#         if sum(c in special_characters for c in password) < 2:
#             print("Weak")
#         else:
#             print("Strong")

# --------------> task 3



# word = "RACECAR"

# if word == word[::-1]:
#     print("Open")
# else:
#     print("Trash")

# --------------> task 4



# string = "hello"

# string_list = []
# for char in string:
#     string_list.append(char)

# print(string_list)

# --------------> task 5



# numbers_str = "12 21 15 19 8"

# numbers_list = numbers_str.split()

# for num_str in numbers_list:
#     num = int(num_str)
#     if num % 2 == 0:
#         print(num, end=" ")

# --------------> task 6



# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# odd_items = []
# index = 0
# while index < len(items):
#     if items[index] % 2 != 0: 
#         odd_items.append(items[index])
#         del items[index]  
#     else:
#         index += 1

# print("Odd Items:", odd_items)

# --------------> task 7



# items = [1, 2, 3, 4, 2, 3, 5, 6, 7, 1]

# unique_items = []

# for item in items:
#     if item not in unique_items:
#         unique_items.append(item)

# print("List with duplicates removed:", unique_items)

# --------------> task 8