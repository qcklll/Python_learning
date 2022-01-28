filename = "guest.txt"
print("Для выхода из программы введите quit")


while True:
    name = input("Введите ваше имя: \n")
    if name == 'quit':
        break
    else:
        print(f"Привет {name}")
        with open(filename,"a") as file_object:
            file_object.write(f'{name}\n')




