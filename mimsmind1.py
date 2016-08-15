import random
import sys

l = 3
try:
  length = sys.argv[1]
  l = int(length)
except ValueError:
  print("{} isn't a number!".format(length))
except IndexError:
  print("No arguments were provided")

maxrounds = 2 ** l + l  

number = random.randint(0, 10 ** l)
print("Let's play the mimsmind1 game. You have {} guesses".format(maxrounds))

guess = input("Guess a {}-digit number: ".format(l))

while maxrounds >= 0:
  guess = int(guess)
  if guess > number:
    guess = input("Try again. Guess a lower number: ")
    maxrounds -=1
  elif guess < number:
    guess = input("Try again. Guess a higher number: ")
    maxrounds -=1
  elif guess == number:
    maxrounds -=1
    print("Congratulations. You guessed the correct number in {} tries.".format(maxrounds))
    break
  else:
    print("Seems like it is not a number. Try next time. Bye!")
    break
print("Sorry, you are out of tries")
