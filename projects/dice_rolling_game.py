# Dice Rolling Game
import random

# Intialise the game
game_on = True
# Loop
while game_on:
  choice = input('Roll the dice? (y/n): ').lower()
  if choice == 'y':
    how_many_rolls = int(input('How many rolls? '))
    for i in range(how_many_rolls):
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      print(f'You rolled a {die1} and a {die2}')
    print(f'Total rolls: {how_many_rolls}')
    game_on = False
  elif choice == 'n':
    print('Thank you for playing!')
    game_on = False
    break
  else:
    print('Invalid choice')

