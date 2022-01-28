print("Введите два числа, я их поделю")
print("Введите 'q' для выхода ")

while True:
    first_number = input("\nВведите первое число")
    if first_number == 'q':
        break
    second_number = input("\nВведите второе число")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Вы не можете делить на ноль")
    else:
        print(answer)
