def binarySearch(selectedGameList, gameID):  #binary search that takes a list and an object and returns true if that object is in the list, and otherwise - false
    if len(selectedGameList) != 0:   
        mid = len(selectedGameList)//2
        if selectedGameList[mid]==gameID:
            return True
        elif gameID < selectedGameList[mid]:
            return binarySearch(selectedGameList[:mid], gameID) # recursion until object is found or none is left 
        else:
            return binarySearch(selectedGameList[mid+1:], gameID)
    else:
        return False
