from random import randint
from pathlib import Path


class Dice:
    def roll(self):
        return randint(1, 6), randint(1, 6)


dice = Dice()
print(dice.roll())

p = Path()

for file in p.glob("*.py"):
    print(file)
