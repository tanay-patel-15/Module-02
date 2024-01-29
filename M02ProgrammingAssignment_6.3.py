guess_me = 5

for i in range(10):
  if i < guess_me:
    print(i, " is too low!")
  elif  i == guess_me:
    print("Found it! ", i, " is correct!")
    break
  elif  i > guess_me:
    print("Oops!")
    break