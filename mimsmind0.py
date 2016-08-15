import random
import sys

print("Let's play the mimsmind0 game.")
l = 1
try:
  length = sys.argv[1]
  l = int(length)
except ValueError:
  print("{} isn't a number!".format(length))
except IndexError:
  print("No arguments supplied!")

count = 0
number = random.randint(1, 10 ** l)

guess = input("Guess a {}-digit number: ".format(l))

while True:
  guess = int(guess)
  if guess > number:
    count +=1
    guess = input("Try again. Guess a lower number: ")
    #continue
  elif guess < number:
    count +=1
    guess = input("Try again. Guess a higher number: ")
    #continue
  elif guess == number:
    count +=1
    print("Congratulations. You guessed the correct number in {} tries.".format(count))
    break
  else:
    print("Seems like it is not a number. Try next time. Bye!")
    break

