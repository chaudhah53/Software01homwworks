import random

num_dice = int(input("How many dice would you like to roll? "))
total = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i+1} rolled: {roll}")
    total += roll

print(f"The total sum of your dice rolls is: {total}")
