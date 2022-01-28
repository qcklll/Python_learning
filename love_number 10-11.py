import json

filename = 'love_number.json'
def get_num():
    number = input("Какое ваше любимое число?")
    with open(filename,'w') as f_obj:
        json.dump(number, f_obj)

def set_num():
    with open(filename) as f_obj:
        user = json.load(f_obj)
    if user:
        print("Я знаю ваше любимое число: " + user)
    else:
        get_num()

get_num()
set_num()

