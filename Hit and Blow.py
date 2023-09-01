import random

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

def Game():
  print("Welcome to Hit and Blow!")
  correct_answer = random.randint(1000, 9999)
  attempts = 0
  
  while True:
    
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

    if attempts > 10:
        quit_choice = input("Do you want to quit? Press y if so. ")
        if quit_choice.lower() == "y":
            print("This is the correct answer:", correct_answer)
            break
        else:
            continue
    
Game()

  
