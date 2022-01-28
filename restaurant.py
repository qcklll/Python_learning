class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        """Создадим два атрибута name & type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_server = 15

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print("Тип кухни " + self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан " + self.restaurant_name.title() + " Открыт!")


class IceCreamStand (Restaurant):
    """Создаёт класс с мороженным"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        for flavor in self.flavors:
            print("Мороженное со вкусом " + flavor)


