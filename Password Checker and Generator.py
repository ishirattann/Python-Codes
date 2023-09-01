import string
import random

# Lowercase
global all
alphabet_lower = string.ascii_lowercase
all = list(alphabet_lower)

# Uppercase
global alh
alphabet_higher = string.ascii_uppercase
alh = list(alphabet_higher)

# Numbers
global numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Allowed characters
global allowed_chars
allowed_chars = ['!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

# Every character 
all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

def Menu():
  print("Hello, and welcome to the Password Checker and Generator!")
  print("Would you like to check a password, generate a password, or quit?")
  choice = input("1 for Check, 2 for Generate and 3 for Quit: ")
  if choice == "1":
    Check()
  elif choice == "2":
    Generate()
  elif choice == "3":
    Quit()
  else:
    print("Invalid input. The menu will repeat again.")
    Menu()

def Check():
  global score_length
  global score1
  global score2
  global score3
  global score4
  global score_allpres
  global overall_score
  score_length = 0
  score1 = 0
  score2 = 0
  score3 = 0
  score4 = 0
  score_allpres = 0
  overall_score = 0
  
  password = input("Please enter your password: ")
  if len(password) < 8 or len(password) > 24:
    print("Invalid input. You will be returned to the menu.")
    
    Menu()
   
  else:
    score_length = len(password)
    password_list = [i for i in password]
    for a in password_list:
      for b in all:
        if a == b:
          score1 = score1 + 5
          break
    if score1 == 5 or score1 > 5:
      score1 = 5
    else:
      score1 = 0
  
  for c in password_list:
    for d in alh:
      if c == d:
        score2 = score2 + 5
        break
    if score2 == 5 or score2 > 5:
      score2 = 5
    else:
      score2 = 0

  for e in password_list:
    for f in numbers:
      if e == f:
        score3 = score3 + 5
        break
    if score3 == 5 or score3 > 5:
      score3 = 5
    else:
      score3 = 0

  for g in password_list:
    for h in allowed_chars:
      if g == h:
        score4 = score4 + 5
        break
    if score4 == 5 or score4 > 5:
      score4 = 5
    else:
      score4 = 0

  if score1 == 5 and score2 == 5 and score3 == 5 and score4 == 5:
    score_allpres = score_allpres + 10

  overall_score = score_length + score1 + score2 + score3 + score4 + score_allpres
  print("Your overall score without point deduction is", overall_score)
  
  if score1 == 5 and score2 == 5 and score3 == 0 and score4 == 0:
    overall_score = overall_score - 5

  if score1 == 0 and score2 == 0 and score3 == 5 and score4 == 0:
    overall_score = overall_score - 5

  if score1 == 0 and score2 == 0 and score3 == 0 and score4 == 5:
    overall_score = overall_score - 5

  global qwerty_sets
  qwerty_sets = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm']
  
  for i in qwerty_sets:
      if i in password.lower():
        overall_score = overall_score - 5

  print("Your overall score after point deduction is", overall_score)

  if overall_score > 20:
    print("This means your password is strong. Now you will be returned to the menu.")
    Menu()
  elif overall_score <= 0:
    print("This means your password is weak. Now you will be returned to the menu.")
    Menu()
  else:
    print("Your password is of a medium strength. Now you will be returned to the menu.")
    Menu()

def Generate():
  global score_length
  global score1
  global score2
  global score3
  global score4
  global score_allpres
  global overall_score
  score_length = 0
  score1 = 0
  score2 = 0
  score3 = 0
  score4 = 0
  score_allpres = 0
  overall_score = 0
  all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
  length = random.randint(8,12)
  password = random.sample(all_chars, length)
  password = ''.join(password)
  print("Your generated password is:", password)
  password_list = [i for i in password]
  for a in password_list:
      for b in all:
        if a == b:
          score1 = score1 + 5
          break
      if score1 == 5 or score1 > 5:
        score1 = 5
      else:
        score1 = 0
  
  for c in password_list:
    for d in alh:
      if c == d:
        score2 = score2 + 5
        break
    if score2 == 5 or score2 > 5:
      score2 = 5
    else:
      score2 = 0

  for e in password_list:
    for f in numbers:
      if e == f:
        score3 = score3 + 5
        break
    if score3 == 5 or score3 > 5:
      score3 = 5
    else:
      score3 = 0

  for g in password_list:
    for h in allowed_chars:
      if g == h:
        score4 = score4 + 5
        break
    if score4 == 5 or score4 > 5:
      score4 = 5
    else:
      score4 = 0

  if score1 == 5 and score2 == 5 and score3 == 5 and score4 == 5:
    score_allpres = score_allpres + 10

  overall_score = score_length + score1 + score2 + score3 + score4 + score_allpres
  print("The overall score of this password without point deduction is", overall_score)
  
  if score1 == 5 and score2 == 5 and score3 == 0 and score4 == 0:
    overall_score = overall_score - 5

  if score1 == 0 and score2 == 0 and score3 == 5 and score4 == 0:
    overall_score = overall_score - 5

  if score1 == 0 and score2 == 0 and score3 == 0 and score4 == 5:
    overall_score = overall_score - 5

  global qwerty_sets
  qwerty_sets = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop', 'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl', 'zxc', 'xcv', 'cvb', 'vbn', 'bnm']
  
  for i in qwerty_sets:
      if i in password.lower():
        overall_score = overall_score - 5

  print("The overall score of this password after point deduction is", overall_score)

  if overall_score > 20:
    print("This means your password is strong. Now you will be returned to the menu.")
    Menu()
  elif overall_score <= 0:
    print("This means your password is weak. The password needs to be strong, so we will generate another password!")
    Generate()
  else:
    print("Your password is of a medium strength. The password needs to be strong, so we will generate another password!")
    Generate()

def Quit():
  print("Goodbye!")
  
Menu()

