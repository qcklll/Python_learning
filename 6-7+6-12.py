# people1 = {'name':'Misha','last_name':'botcman','age':'20'}
# people2 = {'name':'Max','last_name':'churikov','age':'21'}
# people3 = {'name':'Andrei','last_name':'efremov','age':'23'}
# people = [people1,people2,people3]
# for man in people:
#     print("Имя:" + man['name'].title() + " Фамилия:" + man['last_name'].title() + " Возраст:" + man['age'].title() )
# 6-8
# pet1 = {'name':'Jack','animal':'dog','owner':'james'}
# pet2 = {'name':'marta','animal':'cat','owner':'john'}
# pet3 = {'name':'ruby','animal':'rat','owner':'micael'}
# pets = [pet1,pet2,pet3]
# for pet in pets:
#     print("Кличка:" + pet['name'].title() + " Вид животного:" + pet['animal'].title()  + " Хозяин:" + pet['owner'])
# 6-9
# favorite_places = {'Misha':['Moscow'],
#                    'Ilya':['Magadan','Moscow'],
#                    'Max':['Kiev','Melipotol','St.Peterburg']
#                    }
# for n,p in favorite_places.items():
#     print(f" Имя: {n} Любимые места:")
#     for place in p:
#         print("\t" + place.title())
# 6-10 смотри в 6-1
# 6-11
cities = {
    'Moscow':{
        'country':'Russia',
        'population':'12 million',
        'fact':' 99% жителей Москвы - это хачи'
            },
    'Kiev':{
        'country':'Ukraine',
        'population':'8 million',
        'fact':' Не все хохлы любят сало'
            },
    'Сеул':{
        'country':'Korea',
        'population':'999 million',
        'fact':' они похохи на производителей Toyota, но это ложь '
            },
        }
for c, f in cities.items():
    print(f"\nГород: {c}")
    full_inf = f['country'] + f['fact']
    popul = f['population']
    print("Страна и факт: " + full_inf)
    print("Население:" + popul)
