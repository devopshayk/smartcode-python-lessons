# button_mapping = {
#     '.': '1', ',': '1', '?': '1', '!': '1', ':': '1',
#     'A': '2', 'B': '2', 'C': '2',
#     'D': '3', 'E': '3', 'F': '3',
#     'G': '4', 'H': '4', 'I': '4',
#     'J': '5', 'K': '5', 'L': '5',
#     'M': '6', 'N': '6', 'O': '6',
#     'P': '7', 'Q': '7', 'R': '7', 'S': '7',
#     'T': '8', 'U': '8', 'V': '8',
#     'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
#     ' ': '0'
# }

# message = input("Введите сообщение: ")

# sequence = ""

# for char in message:
#     char = char.upper()
#     if char in button_mapping:
#         sequence += button_mapping[char]

# print("Последовательность кнопок:", sequence)

# --------------> task 1



# user_string = input("Введите строку: ")

# unique_characters = set()

# for char in user_string:
#     unique_characters.add(char)

# num_unique_characters = len(unique_characters)

# print("Количество уникальных символов во введенной строке:", num_unique_characters)

# --------------> task 2



# word1 = input("Введите первое слово: ").lower()  
# word2 = input("Введите второе слово: ").lower()  

# if sorted(word1) == sorted(word2):
#     print("Да, введенные слова являются анаграммами.")
# else:
#     print("Нет, введенные слова не являются анаграммами.")

# --------------> task 3