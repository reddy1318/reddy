def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList
newList = [12,4,6,8,9]
print(swapList(newList))