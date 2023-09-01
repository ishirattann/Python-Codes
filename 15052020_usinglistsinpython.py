countrieslist = ["France", "UK", "USA", "Spain"]


# delete a string from a certain position
del countrieslist[3]
print(countrieslist)

# (append means add) append a new country of the user's choice, print list
newcountry = input("Enter another country: ")
countrieslist.append(newcountry)
print(countrieslist)

# using a loop to iterate over text, makes it look neater
newcountry = input("Enter another country: ")
countrieslist.append(newcountry)
for x in countrieslist:
    print(x)

# insert a country at a certain index in the list
countrieslist.insert(4, "Italy")    
print(countrieslist)

# remove a country from the list
countrieslist.remove("USA")
print(countrieslist)

# remove an item from a certain position
countrieslist.pop(2)
print(countrieslist)

# sort the list into alphabetical order
countrieslist.sort()
print(countrieslist)




# correcting code - You have to print the list in order for your choice to show up.
foods = ["pizza", "sandwiches", "pasta", "aubergine", "chicken wings"]

for x in foods:
    print(x)

dislike = input("Enter the food from the list you dislike: ")
foods.remove(dislike)
print(foods)



again = "y"
names = []
while again == "y":
    name = input("Enter a name: ")
    names.append(name)
    again = input("Do you want to enter another name? (y or n)")
print(names)



# 1. Ask the user to enter 3 months of the year and store them in a list. Display the list with each item being displayed on a separate line.

firstmo = input("Enter a month: ")
secondmo = input("Enter another month: ")
thirdmo = input("Enter another month: ")
monthslist = [firstmo, secondmo, thirdmo]
for x in monthslist:
    print(x)


# 2. Save 5 numbers in a list. Add each item in the list to a total and display the total

fiveno = [4, 5, 7, 8, 9]
total = sum(fiveno)
print("The sum of the five numbers is:", total)


# 3. Ask the user to enter 5 names (use a loop to do this if you can). Once all the name have been added sort the list and display it to the user.
# Ask them to enter a number between 0 and 4 and remove the name in that position from the list. Display the list again to the user 

namelist = []
for x in range(5):
    name = input("Enter a name: ")
    namelist.append(name)
    namelist.sort()
for x in namelist:
    print(x)
number = int(input("Enter a number between 0 and 4: "))

namelist.pop(number)
for x in namelist:
    print(x)


# 4. Display 3 colours, each showing on separate lines and ask the user to enter a new colour and a position in the list.
# Insert the colour in the list in the correct position and display the list again.
# Ask the user to name one of the colours in the list and remove that colour from the list and display the list once more ​

colourslist = ["red", "orange", "yellow"]
for x in colourslist:
    print(x)

newcolour = input("Enter another colour: ")
newposition = int(input("Enter another position: "))
colourslist.insert(newposition, newcolour)
for x in colourslist:
    print(x)

listcolour = input("Name one of the colours in the list: ").lower()
#listcolour = listcolour.lower()
colourslist.remove(listcolour)
for x in colourslist:
    print(x)













