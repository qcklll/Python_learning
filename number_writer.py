import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open('numbers.json', 'w') as f_obj:
    json.dump(numbers, f_obj)
