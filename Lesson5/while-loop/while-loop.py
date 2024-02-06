# rows = int(input('Write num for rows: '))
# cols = int(input('Write num for cols: '))

# for i in range(rows):
#     for j in range(cols):
#         if i % 2 == 0:
#             print(i + 2 * j, end=' ')
#         else:
#             print(i + 2 * j + 1, end=' ')
#     print()

# --------------> task 1



# rows = 5

# for i in range(1, rows + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# --------------> task 2



# rows = 4
# cols = 20

# for i in range(rows):
#     if i == 0 or i == rows - 1:
#         print('|' + '-' * (cols - 2) + '|')
#     else:
#         print('|' + ' ' * (cols - 2) + '|')

# --------------> task 3



# count = int(input("Enter the number of integers: "))
# prime_count = 0
# current = 0

# while current < count:
#     num = int(input("Enter a number: "))
#     is_prime = True
#     if num <= 1:
#         is_prime = False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#     if is_prime:
#         prime_count += 1
#     current += 1

# print("The number of prime numbers in the sequence:", prime_count)

# --------------> task 4



# N = int(input("Enter the number N: "))

# factorial_sum = 0
# factorial = 1

# for i in range(1, N + 1):
#     factorial *= i
#     factorial_sum += factorial

# print("The sum of factorials from 1! to", N, "! =", factorial_sum)

# --------------> task 5



# N = int(input("Enter the number of natural numbers: "))

# max_sum_digits = 0
# number_with_max_sum = 0

# for _ in range(N):
#     num = int(input("Enter a natural number: "))
#     temp_num = num
#     sum_digits = 0
#     while temp_num > 0:
#         sum_digits += temp_num % 10
#         temp_num //= 10
#     if sum_digits > max_sum_digits:
#         max_sum_digits = sum_digits
#         number_with_max_sum = num

# print("The number with the largest sum of digits is:", number_with_max_sum)
# print("The sum of its digits is:", max_sum_digits)

# --------------> task 6



# rows = 4

# for i in range(1, rows + 1):
#     print(" " * (rows - i) + "#" * (2*i - 1))

# --------------> task 7