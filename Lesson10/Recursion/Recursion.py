import random
import os

crab_i = random.randint(1, 19)
crab_j = random.randint(1, 19)
worm_i = random.randint(1, 19)
worm_j = random.randint(1, 19)
points = 0

while True:
    for i in range(21):
        for j in range(21):
            if i == crab_i and j == crab_j:
                print('🦀', end='')
            elif i == worm_i and j == worm_j:
                print('🐛', end='')
            else:
                print('🌊', end='')
        print()
    print(f'Points -> {points}')
    
    if points == 5:
        print('You win')
        break
    
    move = input("Enter move (W/A/S/D to move, Q to quit): ").upper()
    
    if move == 'W':
        crab_i -= 1
    elif move == 'S':
        crab_i += 1
    elif move == 'A':
        crab_j -= 1
    elif move == 'D':
        crab_j += 1
    elif move == 'Q':
        break
    
    if crab_i == worm_i and crab_j == worm_j:
        worm_i = random.randint(1, 19)
        worm_j = random.randint(1, 19)
        points += 1
    os.system('clear')  # Use 'clear' for Unix/Linux, 'cls' for Windows
