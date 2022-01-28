my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods [:]
my_foods.append('pelmeni')
friend_foods.append('salo')


print("My favori foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("The first three items in the list are:")
print(my_foods[:3])
print("The  middle three items in the list are:")
print(my_foods[0:3])
print("The  last three items in the list are:")
print(my_foods[-3:])

for food in my_foods:
    print("My favorite food " + food)
for ffood in friend_foods:
    print("Любимые блюда у моего друга это: " + ffood)

