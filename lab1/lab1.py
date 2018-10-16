def getStrList(filename):
    f = open(filename)
    return [line for line in f];


def makeInverseIndex(strlist):
    tempList = [(i, j.split()) for (i, j) in enumerate(strlist)]
    tempSet = set()
    for item in strlist:
        tempSet.update(set(item.split()))

    dictionary = {}
    for word in tempSet:
        newSet = set()
        for (i, j) in tempList:
            if word in j:
                newSet.add(i)

        dictionary[word] = newSet

    return dictionary;


listA = getStrList('stories_small.txt')
listB = getStrList('stories_big.txt')

dictionaryA = makeInverseIndex(listA)
dictionaryB = makeInverseIndex(listB)
