import random

#define variables
dice_rolls = 2

#function definition
def main(dice_rolls):
    dice_sum = 0
    for i in range(dice_rolls):
        roll = random.randint(1, 6)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll} critical failure')
        elif 1 < roll < 6:
            print(f'You rolled a {roll}')
        else:
            print(f'You rolled a {roll} critical success')
    print(" You have rolled a total of {}".format(dice_sum))


if __name__ == "__main__":
    main(dice_rolls)
