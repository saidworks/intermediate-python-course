import random

#define variables
dice_rolls = 2

#function definition
def main(dice_rolls):
    dice_sum = 0
    for i in range(dice_rolls):
        roll = random.randint(1, 6)
        dice_sum += roll
        print(f'You rolled a die {roll}')
    print(" You have rolled a total of {}".format(dice_sum))


if __name__ == "__main__":
    main(dice_rolls)
