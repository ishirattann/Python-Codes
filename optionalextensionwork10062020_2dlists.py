# Write a program that:

timetable = []

#Monday
timetable.append(["History","Maths","Computer Science","PE","Music"])
#Tuesday
timetable.append(["English","Spanish","Maths","Geography","Art"])
#Wednesday
timetable.append(["PE","English","Science","Art","PE"])
#Thursday
timetable.append(["Maths","English","Philosohpy","Spanish","Music"])
#Friday
timetable.append(["Science","Drama","History","Geography","Science"])

# Asks the user to input a day of the week (e.g. Tuesday)
# Asks the user to input a period of the day (between 1 and 5) (e.g. 2)
# Retrieve and outputs the lesson on that day and period (e.g. Spanish)

someday = input("Please enter a day from Monday to Friday: ")
someperiod =int(input("Please enter a period that you want to see (between 1 and 5): "))
while someperiod<1 or someperiod>5:
    someperiod =int(input("Please enter a period that you want to see (between 1 and 5): "))

if someday == "Monday":
    lesson = timetable[0][someperiod-1]
    print(timetable[0][someperiod-1])
elif someday == "Tuesday":
    lesson = timetable[1][someperiod-1]
    print(timetable[1][someperiod-1])
elif someday == "Wednesday":
    lesson = timetable[2][someperiod-1]
    print(timetable[2][someperiod-1])
elif someday == "Thursday":
    lesson = timetable[3][someperiod-1]
    print(timetable[3][someperiod-1])
elif someday == "Friday":
    lesson = timetable[4][someperiod-1]
    print(timetable[4][someperiod-1])
    

















