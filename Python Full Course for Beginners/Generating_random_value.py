import random

memders = ['john','mary','bob','raktim']
dice = ['1','2','3','4','5','6']
roll_dice1 = random.choices(dice)
roll_dice2 = random.choices(dice)
leader = random.choice(memders)
# print(roll_dice)
print(f'{roll_dice1} {roll_dice2}')
for i in range(3):
    print(random.randint(10,20))


class Dice:
    def roll(self):
        first = random.randint(1,6)
        secound = random.randint(1,6)
        return [first,secound]


dice = Dice()
print(dice.roll())