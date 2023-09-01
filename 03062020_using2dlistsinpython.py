# 1.
# Create a program that will ask the user to input a name and a salary
# and store them in a 2D list.
# After each data is added ask if they want to add another and
# keep repeating this loop until they answer “no”.
# Finally, display the full 2D list.

again = "yes"
together = []
while again == "yes":
    name, salary = input("Enter a name: "), int(input("Enter a salary: "))
    two = [name, salary]
    together.append(two)
    again = input("Do you want to enter more? (yes or no): ")

print(together)

# 2.
# Alter your previous program so once the list is created
# it will ask the user to input a name and display the salary for that name.
# If they enter a name that is not in the list it should display the message “Not in list”.

again = "yes"
together = []
while again == "yes":
    name, salary = input("Enter a name: "), int(input("Enter a salary: "))
    two = [name, salary]
    together.append(two)
    again = input("Do you want to enter more? (yes or no): ")

name1 = input("Enter a name that you want to see the salary for: ")
if name1 == name:
    print(salary)
else:
    print("Not in list.")

