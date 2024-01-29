guess_me = 7
number = 1

while True:
  if number < guess_me:
    print(number, " is too low!")
  elif  number == guess_me:
    print("Found it! ", number, " is correct!")
    break
  elif  number > guess_me:
    print("Oops!")
    break
  number  += 1