# def city_country(city_name,country_name):
#     c_c = {'city': city_name, 'country':country_name}
#     if isinstance(country_name, str):
#         print(f'{city_name},{country_name}')
#     return 'Страна - не может быть числом'
#city_country("Москва","Россия")
# print(city_country('МАСКВА',country_name=1))
#8-7 + 8-8
# def make_album(name,album,track=''):
#     music = {'name': name, 'album':album}
#     if track =='':
#         q = 0
#         print(f'Исполнитель: {name}, название альбома: {album}')
#     elif isinstance(track,int):
#         music['track'] = track
#         print(f'Исполнитель: {name}, название альбома: {album}, '
#               f'Количество дорожен: {track}')
#     else:
#         return 'Track не число'
#     full_music = name + ' ' + album
#     return full_music
#
# while True:
#     print("Введите название исполнителя и альбом")
#     print("(enter 'q' at any time to quit)")
#     n = input("Исполнитель:")
#     if n == 'q':
#         break
#     a = input("Альбом: ")
#     if a == 'q':
#         break
#
#     mus = make_album(n,a)
#     print("Исполнитель + название альбома: " + mus)
# make_album('Noize mc','Hard reboot')
# make_album('Nirvana','bleach', track = 13)
# print(make_album('aboba','aboba','sss'))
# Пример из книги
# def get_formatted_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# Бесконечный цикл!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")
# 8-9
# def show_magicians(names):
#     """"Выводит имя фокусника """
#     for name in names:
#         msg = f"Привет фокусник: {name}"
#         print(msg)
# focus = ["Эмиль Кио","Гарри Гудини","Ури Геллер"]
# show_magicians(focus)
# 8-10
# def show_magicans(people):
# 	for magican in people:
# 		print(magican.title() + " showed a trick")
# def make_great(people):
# 	for magican in people:
# 		magican = "Great " + magicans.pop(0)
# 		people.append(magican)
# 	return people
# 
# magicans = [ "Fred", "Mike", "Freddy"]
# 
# show_magicans(make_great(magicans))
# 8-12
# def sandwich(*components):
# 	print(components)
# sandwich('рыба')
# sandwich('сыр','бекон')
# sandwich('сыр','бекон','соус')
# 8-13
# def build_profile(first, last, **user_info):
# 	profile = {}
# 	profile['first_name'] = first
# 	profile['last_name']  = last
# 	for key,value in user_info.items():
# 		profile[key] = value
# 	return profile
#
# user_profile = build_profile('albert', 'einstein',
# 							location='princeton',
# 							field='physics')
# print(user_profile)
#8-14
# def car (manufacturer,brand,**car_make):
# 	cars = {}
# 	cars ['Производитель'] = manufacturer
# 	cars ['Марка авто']	   = brand
# 	for key,value in car_make.items():
# 		cars[key] = value
# 	return cars
#
# machine = car('lada','priora',
# 			  region = 'Moskva',
# 			  dvigatel = '16 litrov')
# print(machine)




