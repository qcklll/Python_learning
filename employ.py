class Employee():
    def __init__(self, name, l_name, sallary):
        self.name = name
        self.l_name = l_name
        self.sallary = sallary

    def give_raise(self, give=5000):
        x = (self.sallary * 12) + give
        return x
