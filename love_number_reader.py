import json

filename = 'love_number.json'
with open(filename) as f_obj:
   a = json.load(f_obj)

print("Ваше любимое число: " + a)