class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.color = input('Введите цвет вашей кошки')

    def cat_eat(self):
        print("Кис-кис" + self.name + "иди кушать")

    def show_age(self):
        print("Моей кошке " + str(self.age) + " лет")

    def show_color(self):
        print("Какого цвета твоя кошка? " + self.color)


my_cat = Cat('Матильда', 6)
my_cat.show_age()
my_cat.color
my_cat.show_color()

