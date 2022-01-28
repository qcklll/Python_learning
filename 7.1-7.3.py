#7-1
# text = "Let me see if I can find you a"
# venichle = input(text)
#7-2
# restoran = input("На сколько человек вам нужен стол?")
# restoran = int(restoran)
#
# if restoran > 8:
#     print("Извините, вам придётся немного подождать")
# else:
#     print("Ваш стол готов")
#7-3
# number = input("Введите ваше число: ")
# number = int(number)
#
# if number % 10==0:
#     print("Ваше число кратно 10")
# else:
#     print("Число не кратное 10"
import math
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

