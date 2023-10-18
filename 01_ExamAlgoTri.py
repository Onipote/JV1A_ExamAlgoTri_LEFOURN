myTable = [6, 8, 2, 10, 4]
stock = 0

stock = myTable[3]
myTable[3] = myTable[1]
myTable[1] = stock

print(myTable)