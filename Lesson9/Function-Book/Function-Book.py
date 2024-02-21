# def binary_to_decimal(binary_str):
#     decimal = 0
#     power = len(binary_str) - 1
#     for digit in binary_str:
#         if digit == '1':
#             decimal += 2 ** power
#         power -= 1
#     return decimal

# def main():
#     binary_str = input("Введите число в двоичном виде: ")
#     if set(binary_str) - {'0', '1'}:
#         print("Ошибка: введенное значение не является двоичным числом.")
#     else:
#         decimal = binary_to_decimal(binary_str)
#         print("Десятичное представление числа", binary_str, ":", decimal)

# if __name__ == "__main__":
#     main()


# --------------> task 1



# def decimal_to_binary(decimal):
#     if decimal < 0:
#         print("Ошибка: введено отрицательное число.")
#         return None

#     result = ""
#     q = decimal

#     if q == 0:
#         return "0"

#     while q != 0:
#         r = q % 2
#         result = str(r) + result
#         q //= 2

#     return result

# def main():
#     decimal = int(input("Введите целое число в десятичной системе: "))
#     binary = decimal_to_binary(decimal)
#     if binary is not None:
#         print("Двоичное представление числа", decimal, ":", binary)

# if __name__ == "__main__":
#     main()

# --------------> task 2



# BASE_FARE = 4.00  
# RATE_PER_KM = 0.25  

# def taxi_fare(distance_km):
#     distance_m = distance_km * 1000  
#     additional_fare = (distance_m / 140) * RATE_PER_KM  
#     total_fare = BASE_FARE + additional_fare  
#     return total_fare

# def main():
#     distance = float(input("Введите расстояние поездки в километрах: "))
#     fare = taxi_fare(distance)
#     print("Итоговая сумма оплаты за поездку на такси: ${:.2f}".format(fare))

# if __name__ == "__main__":
#     main()

# --------------> task 3