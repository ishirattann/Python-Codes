# question 1

ID = [45, 33, 27, 88, 103, 66, 71]
numberSought = int(input("Please enter ID number to find "))
found = False
n = len(ID)
k = 0
while (found is False) and (k < n):
    if numberSought == ID[k]:
        found = True
        break
    k = k + 1
if found == True:
    print("ID is in the list at index ", k)
else:
    print("ID is not in the list.")

# question 2

monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthBill = []
i = 0
for x in range(0,12):
    bill = float(input("Enter bill for " + monthName[i] + " "))
    monthBill.append(bill)
    i = i + 1
maxNum = 0
for j in monthBill:
    if j > maxNum:
        maxNum = j
valueNeeded = monthBill.index(maxNum)
print("The month with maximum amount is " + monthName[valueNeeded] + " and the maximum amount is", maxNum)

# question 3

product = 0
month = 0
j = 0
sum = 0
sales = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
totalSales = []
for product in range(5):
    print("Sales for product", product + 1)
    for month in range(3):
        sales[month][product] = int(input("Enter quantity for month: "))
for product in range(5):
    sum = 0
    for month in range(3):
        j = sales[month][product]
        sum = sum + j
    totalSales.append(sum)
for n in range(5):
    print("Total for product", n + 1, "is", totalSales[n])

    
