import random

number_to_guess = random.randint(1, 100)

while True:
  try:
    user_guess = int(input('Guess the number between 1 and 100: '))
    # print(f'You guessed {user_guess}')
    if user_guess == number_to_guess:
      print('Congratulations! You guessed it!')
      break
    elif user_guess > number_to_guess:
      print('Too high')
    else:
      print('Too low')
  except ValueError:
    print('Please enter a valid number')


