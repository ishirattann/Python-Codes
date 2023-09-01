students = int(input("Number of students? "))
teachers = int(input("Number of teachers? "))
participants = students + teachers
print("Total number of participants:", participants)
largeBuses = participants // 46
print("Number of large buses:", largeBuses)
remainder = participants % 46
smallBuses = remainder // 16
remainder = remainder % 16
if remainder > 0:
    smallBuses = smallBuses + 1
    print("Number of large buses:", smallBuses)
    totalCost = largeBuses * 360 + smallBuses * 140
    print("Total cost:", totalCost)
else:
    print("Number of small buses:", smallBuses)
    totalCost = largeBuses * 360 + smallBuses * 140
    print("Total cost:", totalCost)



