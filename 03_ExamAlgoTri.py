myTable = [6, 8, 2, 10, 4]
max = myTable[0]
pasTrie = True
print(myTable)

#repeter la boucle jusqu'a ce que tout soit dans l'ordre croissant
while(not pasTrie):
    for i in range(len(myTable)):
        if myTable[i-1] < myTable[i] > max: #si val i est supérieure a val i+1
            max = myTable[i] #max prend la valeur de l'indice actuel
            myTable[i] = myTable[4] #l'indice actuel prend la valeur du dernier indice (fin liste)
            myTable[4] = max #le dernier indice prend la valeur de max
        


print(myTable)