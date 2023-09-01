import random
'''
first = random.randint(1,6)
second = random.randint(1,6)
total = first + second
print(first, second, total)
'''
#PORO is Player One Roll One. PORT is Player One Roll Two.

first_score = 0
PORO = random.randint(1,6)
PORT = random.randint(1,6)
print(PORO)
print(PORT)
if PORO > PORT:
    first_score = (PORO + PORT)
elif PORO < PORT:
    first_score = (PORO + PORT)
elif PORO == PORT:
    first_score = (2 * PORO + PORT)
elif PORO and PORT == 6:
    print("First player's score is zero. Tough luck.")
print(first_score)

#PTRO is Player Two Roll One. PTRT is Player Two Roll Two.

second_score = 0
PTRO = random.randint(1,6)
PTRT = random.randint(1,6)
print(PTRO)
print(PTRT)
if PTRO > PTRT:
    second_score = (PTRO + PTRT)
elif PTRO < PTRT:
    second_score = (PTRO + PTRT)
elif PTRO == PTRT:
    second_score = (2 * PTRO + PTRT)
elif PTRO and PTRT == 6:
    print("Second player's score is zero. Tough luck.")
print(second_score)

if first_score > second_score:
    print("The first player is the winner!")
elif first_score < second_score:
    print("The second player is the winner!")
elif first_score == second_score:
    print("You drew!")
    




