class User:

    def __init__(self, first_name, last_name, age, city):
        """Инициализация атрибутов"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Вывод некотой информации о пользователе"""
        print("Имя пользователя: " + self.first_name)
        print("Фамилия пользователя: " + self.last_name)
        print("Возраст: " + str(self.age))
        print("Родной город: " + self.city)

    def greet_user(self):
        print("\n Hello " + self.first_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0