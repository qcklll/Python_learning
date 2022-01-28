# 7.8
# sandwich_orders = ['With fish','With bacon','with chicken','WIth chocolate']
# finished_sandwich = []
#
# for sand in sandwich_orders:
#     print ("I made your sandwich " + sand.lower())
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#
#     print("\nConfirm order " + current_sandwich.lower())
#     finished_sandwich.append(current_sandwich)
# for final in finished_sandwich:
#     print("Your sandwich is made " + final.lower())
#7-9
# print("Извините, мне очень жаль, но бастрамы больше нет")
# sandwich_orders = ['pastrami','With fish','With bacon','Pastrami','with chicken','Pastrami']
#
# sandwich_orders = [w.lower() for w in sandwich_orders]
# print(sandwich_orders)
#
#
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami'.lower())
#
# print(sandwich_orders)

# responses = {}
#
# poling_active = True
# while poling_active:
#     name = input("\nКак вас зовут?")
#     response = input("Где бы вы хотели отдохнуть?")
#     responses[name] = response
#     repeat = input("Хочет ли кто нибудь ещё указать место для отдыха? (yes/no)")
#     if repeat == 'no':
#         poling_active = False
#     for name, response in responses.items():
#         print(name + " его любимое место отдыха: " + response)