# name = "“Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself. \n Bill Gates”"
# def text(name):
#     return name
# print(text(name))

# def even_numbers(start, end):
#     if start > end:
#         start, end = end, start
#
#     for num in range(start + 1, end):
#         if num % 2 == 0:
#             print(num)
#
# even_numbers(3, 10)

# def display_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):
#             print(symbol * side_length)
#     else:
#         print(symbol * side_length)
#         for _ in range(side_length - 2):
#             print(symbol + " " * (side_length - 2) + symbol)
#         print(symbol * side_length)
#
# display_square(5, "*", True)

# def find_minimum(num1, num2, num3, num4, num5):
#     return min(num1, num2, num3, num4, num5)
# result = find_minimum(10, 5, 3, 4, 7)
# print(result)

# def calculate_product(start, end):
#     if start > end:
#         start, end = end, start
#     product = 1
#     for num in range(start, end + 1):
#         product *= num
#     return product
# result = calculate_product(1, 5)
# print(result)


# numbers = 3414
# def scores(numbers):
#     return len(str(numbers))
# print(scores(numbers))


# def is_palindrome(number):
#     number_str = str(number)
#     reversed_str = number_str[::-1]
#     return number_str == reversed_str
#
# result = is_palindrome(123321)
# print(result)