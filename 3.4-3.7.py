gosti = ['Nastya','Irina','Vladimir','Sergei']
priglos = "Приходите ко мне на праздник:"

print(priglos + gosti[0])
print(priglos + gosti[1])
print(priglos + gosti[2])
print(priglos + gosti[3])

#3.5
print (gosti[3] + " Прийти не сможет")
gosti [3] = 'Ilya'

print ("Вместое него придёт: " + gosti[3])

#3.6
print("У меня появилось больше места для гостей")
gosti.insert(0, 'Pavel')
gosti.insert(2, 'Max')
gosti.append('Nikolai')

print(priglos + gosti [0])
print(priglos + gosti [2])
print(priglos + gosti [-1])
a = (len(gosti))
print(gosti)
print(a)


#3.7
print("На обед приглашаются всего два гостя")
ms = "Извините, но я занят сегодня не смогу"
a = gosti.pop()
print(a +" "+ ms)
b = gosti.pop()
print(b +" "+ ms)
c = gosti.pop()
print(c +" "+ ms)
d = gosti.pop()
print(d +" "+ ms)
e = gosti.pop()
print(e +" "+ ms)

del gosti[1]
del gosti[0]
print(gosti)

