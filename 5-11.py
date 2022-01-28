# User = ['admin','nikolay','kevin','max','alexander']
#
# if User:
#     for Users in User:
#         if Users == 'admin':
#             print("Hello admin, whould you like to see a status report?")
#         else:
#             print("Hello " + Users)
# else:
#     print("We need to find some users!")
# 5-10
# current_users = ['aboba','Piter','Valeri','John','Jool']
# new_users = ['ABOBA','VALERI','Kevin','Darius','Kaxa8933']
#
# for ban_list in new_users:
#     if ban_list.lower() in [i.lower() for i in current_users]:
#         print("Пользователь с таким именем уже зарегистрирован")
#     else:
#         print("Такое имя разрешено")
# 5-11
numb = list(range(1,10))
print(numb)
for numbers in numb:
    if numbers == 1:
        print("1st")
    elif numbers == 2:
        print("2nd")
    elif numbers == 3:
        print("3rd")
    else:
        print(f"{numbers}th")