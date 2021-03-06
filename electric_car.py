"""Простая модель электромобился"""
from car import Car


class Battery:
    """Простая модель аккумулятора автомобиля"""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        """Увеличивает мощность аккумулятора"""
        if self.battery_size != 85:
            print("Увеличиваем мощность аккумулятора...")
            self.battery_size = 85
        return self.battery_size


class ElectricCar(Car):
    "Представляет аспекты машины, специфические для электромобилей"

    def __init__(self, make,model, year, color = ''):
        """Инициализирует атрибуты класса родителя"""
        super().__init__(make, model, year)


my_elect = ElectricCar('Tesla','model-x',2018)
print(my_elect.get_descriptive_name())