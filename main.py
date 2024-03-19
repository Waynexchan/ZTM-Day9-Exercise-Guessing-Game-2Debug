from random import randint
import sys
# generate a number 1~10

# input from user?
# check that input is a number 1~10

def guess_input(guess, answer):
  try:
    if  guess !='' and guess!= None and 0 < guess < 11:
      if guess == answer:
          print('you are a genius!')
          return True
    else:
      print('hey bozo, I said 1~10')
      return False
  except ValueError as err:
      return err
      
if __name__ == '__init__':
  answer = randint(1, 10)
  while True:
      try:
          guess = int(input('guess a number 1~10:  '))
          guess_input(guess, answer)
      except ValueError:
          print('please enter a number')
          continue