class Privileges:

    def __init__(self, ):
        self.privileg = []

    def show_privileges(self):
        for pri in self.privileg:
            print("Доброе утро Admin, ваши права: " + pri)
