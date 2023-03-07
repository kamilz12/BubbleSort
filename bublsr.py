def bubbleSort(sortedList):
    listLen = len (sortedList)
    for i in range (listLen - 1):
        for j in range (listLen - 1):
            if sortedList [j] > sortedList [j+1]:
                tempVar = sortedList [j+1]
                sortedList [j+1] = sortedList [j]
                sortedList [j] = tempVar
    return sortedList

def fileToList (fileName):
    file = open (fileName, 'r+') 
    if file.readable ():
        lista1 = file.readlines () 
    file.close () 
    return lista1

#Files are saved in the file with \n, so we have to strip \n and then convert string number to int number
def convertListToIntAndStrip (nonConvertedList):
    convertedList = []
    for i in range (len (nonConvertedList) - 1):
        convertedList.append (nonConvertedList [i].strip ('\n'))
        convertedList [i] = int (convertedList [i])
    return convertedList

def saveListToFile (savedList, saveFileName):
    file = open (saveFileName, "w")
    if file.writable(): #sprawdzenie czy plik jest zapisywalny 
        for i in range (len (savedList)):
            print (savedList, [i], file=file) #aby zapisac plik wystarczy otworzyc plik, nastepnie uzyc funkcji  
    file.close()                    #print ('to co chcemy zapisac do naszego pliku', file=nazwa pliku), nalezy pamietac by na koniec go zamknac
    
beforeSortFile = ('sort.txt')
afterSortFile = ('aftersort.txt')

listFromFile = fileToList(beforeSortFile)
listFromFile = convertListToIntAndStrip(listFromFile)
print (bubbleSort (listFromFile))
saveListToFile (listFromFile, afterSortFile)

