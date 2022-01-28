from random import randint


class Diсe:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, x, y):
        while y < 10:
            x = randint(1, self.sides)
            y += 1
            print("На кубике выпало:" + str(x))


cub = Diсe(20)
cub.roll_dice(0, 0)
