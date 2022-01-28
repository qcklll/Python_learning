while True:
    try:
        a = int(input("Введите число 1"))
        b = int(input("Введите число 2"))
        print(a + b)
    except ValueError: #да да тут ошибка ValueError,а не TypeError
        print("Вы не можете складывать строку с числом")



# Решение из инета
# c = "<class 'int'>"
# try:
#     a, b = int(input()), input()
#     print(a + b)
# except TypeError:
#     if type(a) != c:
#         a = int(a)
#     if type(b) != c:
#         b = int(b)
#     print(a + b)
