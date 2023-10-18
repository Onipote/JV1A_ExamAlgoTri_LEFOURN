myTable = [6, 8, 2, 10, 4]
max = myTable[0] #maximum par defaut
print(myTable)

#permutation val dernier indice (fin de liste) avec indice actuel (si maximum) pour une iteration
for i in range(len(myTable)):
    if myTable[i] > max: #si val i est supérieure a val i+1
        max = myTable[i]
        myTable[i] = myTable[4]
        myTable[4] = max

print(myTable)