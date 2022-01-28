list_pizza = ['4 сыра', "Халапеньо","Гавайская","пепперони"]
for pizza in list_pizza:
    print("\nЯ действительно люблю пиццу:" + pizza)
print("\nДействительно пицца - это вкусно")
friend_pizza = list_pizza[:]
list_pizza.append('Сладкая')
friend_pizza.append('Морская')
print(list_pizza)
print(friend_pizza)
#4-2

# pets = ['dog','horse','rat']
# for pet in pets:
#     print("A " + pet + " would make a great pet")
# print("Любое животное это прекрасно")
