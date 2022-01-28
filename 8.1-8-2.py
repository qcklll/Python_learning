# 8-1
# def display_message():
#     print("Функции")
# display_message()
# 8-2
# def favorite_books(title = "Анна Каренина"):
#     print("Моя любимая книга называется " + title)
# favorite_books('Война и мир')
# 8-3 + 8-4
# def make_shirt (size = 'L', name = 'Python'):
#     print(f"Размер футболки: {size}\nТекст на футболке: {name}")
# make_shirt('xs','I love aboba')
# make_shirt(name="я люблю какать",size='XXL')
# make_shirt()
# make_shirt('S','I LOVE PENI')
# 8-5
# def describe_city(city,country = "Абобия"):
#     print(f'{city.capitalize()} - этот город находится в {country.capitalize()}')
# describe_city('москва','россии')
# describe_city(country="Aboba", city="Bogdanchik")
# describe_city('Самара')
# Пример из книги + изменения с киберфорума
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if isinstance(age, int):
        person['age'] = age
        return person
    return 'age не число'


musician = build_person('jimi', 'hendrix', age=54)
print(musician)
