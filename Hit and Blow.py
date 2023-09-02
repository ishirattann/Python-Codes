import random

# Determining how many hits and blows the user has achieved based on the guess

def Return_Hits_Blows(go, correct_answer):
  hits = 0
  blows = 0
  go = str(go)
  correct_answer = str(correct_answer)
  for y in range(0,4):
    if go[y] == correct_answer[y]:
      hits += 1
    elif go[y] in correct_answer:
      blows += 1
  
  return hits, blows

# Actual game

def Game():
  print("Welcome to Hit and Blow!")
  
# Generate a random 4-digit number, ensuring that the number does not have a leading 0, as that is not a valid 4-digit number
  
  digits = list(range(10))
  random.shuffle(digits)
  correct_answer = digits[:4]
  while correct_answer[0] == 0:
    random.shuffle(digits)
    correct_answer = digits[:4]
    
  attempts = 0
  
  while True:
# Check if the user-inputted go's length is not 4, then ask them to input a number that has 4 digits.
    go = int(input("Enter your go: "))
    if len(str(go)) != 4:
      print("Invalid. Enter a 4-digit number.")
      continue 
    
    attempts += 1 

    hits, blows = Return_Hits_Blows(go, correct_answer)

    if hits == 4:
      print(f"You've guessed the correct answer, {correct_answer} in {attempts} attempts.")
      break
    else:
      print(f"Hits: {hits} Blows: {blows}")
    
Game()

  
