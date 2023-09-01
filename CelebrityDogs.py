import random
decks = []
pd = []
cd = []

def PlayGame():
    read_rules = input("Would you like to read the rules? (y or n) ").lower()
    #The program will give the option to the player to read the rules
    if read_rules == "y":
      print("It's quite simple! This game is all about beating the computer with your deck of cards against its. The amount of cards you choose will be split into two separate decks, one for the computer and another for you. They will all have Celebrity Dogs, with randomly assigned values for their traits: Exercise, Intelligence, Friendliness and Drool in this order. Starting the game, you will be shown the first card in the computer's pile. You then need to pick a trait from the four listed above. Your aim is to get a higher value than the computer if your chosen trait is Exercise, Intelligence or Friendliness. If you chose Drool, then you need a lower value to win the round. If you win the round, then both cards from the computer and the player will be moved to the bottom of your pile. If the computer won, both move to the computer's pile. This repeats until you or the computer has all the cards. Whoever has all of them wins the game! Simple enough? ")
    else:
      print("That's ok, let's get on with the game!")
    global no_of_cards_played
    no_of_cards_played = int(input("Enter the number of cards to be played: "))
    if no_of_cards_played < 4 or no_of_cards_played > 30 or no_of_cards_played % 2 != 0:
      print("Invalid input, you will be returned to the menu.")
      Quit()
      gen_pile(no_of_cards_played)
      
def Quit():
    print("Goodbye!")

def Menu():
    print("Hello and welcome to Celebrity Dogs!")
    want_to_play = input("Would you like to play? (y or n) ").lower()
    if want_to_play == "y":
        PlayGame()
    else:
        Quit()

def gen_pile(no_of_cards_played):
    file = open("dogs.txt", "r").readlines()
    for y in range(30):
      name = file[y].strip()
      decks = gen_card(name)
    random.shuffle(decks)
    k = int(no_of_cards_played/2)
    for i in range(0, k):
        #pd = playerdeck
        pd.append(decks[i])
        #cd = computerdeck
        cd.append(decks[k+i])
    card_numbers(pd, cd)
     
def gen_card(name):
  exercise = random.randint(1, 5)
  intelligence = random.randint(1, 100)
  friendliness = random.randint(1, 10)
  drool = random.randint(1, 10)    
  new_data = [name, exercise, intelligence, friendliness, drool]
  decks.append(new_data)
  return(decks)

def card_numbers(pd, cd):
  while len(pd) != 0 and len(cd) != 0:
    playercard = pd.pop(0)
    computercard = cd.pop(0)
    winner = turn(playercard, computercard) 
    if winner == "The player has won!":
      pd.append(playercard)
      pd.append(computercard)
      print("You win the round!")
    else:
      cd.append(playercard)
      cd.append(computercard)
      print("You lose the round")
  if len(pd) == 0:
    print("You lose the game")
  else:
    print("You win the game")

def turn(playercard, computercard):
  print(playercard)
  choice = input("Enter 1 for Exercise, 2 for Intelligence, 3 for Friendliness, 4 for Drool! ")
  print(computercard)
  if choice == "1":
    if playercard[1] > computercard[1]:
      return "The player has won!"
    else:
      return "The computer has won..."
  elif choice == "2":
    if playercard[2] > computercard[2]:
      return "The player has won!"
    else:
      return "The computer has won..."
  elif choice == "3":
    if playercard[3] > computercard[3]:
      return "The player has won!"
    else:
      return "The computer has won..."
  elif choice == "4":
    if playercard[4] < computercard[4]:
      return "The player has won!"
    else:
      return "The computer has won!"
  else:
    print("Enter 1, 2, 3 or 4")
    return turn(playercard, computercard)
    
Menu()
gen_pile(no_of_cards_played)  
