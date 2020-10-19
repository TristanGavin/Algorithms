# search a bitonic array for a number k

#recursion of each half

def findBitonic(array):
    n = len(array)-1
    m = n//2
    check = array[m]
    aboveCheck = array[m+1]
    belowCheck = array[m-1]
    # if bitonic point
    if aboveCheck < check and belowCheck < check:
        bitonic = m
        return bitonic
    # if check is smaller than point
    elif aboveCheck > check and belowCheck < check:
        findBitonic(array[m:])
    # if check index is larger than point
    elif aboveCheck < check and belowCheck > check: 
        findBitonic(array[:m])
    

def searchLeft(array, k):
    n = len(array)-1
    m = n//2    # if bitonic point
    check = array[m]
    if check == k:
        return m
    # if check is smaller than point
    elif check < k:
        searchLeft(array[m:],k)
    # if check index is larger than point
    elif check > k: 
        searchLeft(array[:m],k)

def searchRight(array, k):
    n = len(array)-1
    m = n//2    # if bitonic point
    check = array[m]
    if check == k:
        return m
    # if check is smaller than point
    elif check > k:
        searchLeft(array[m:],k)
    # if check index is larger than point
    elif check < k: 
        searchLeft(array[:m],k)
    

##### Driver Code

a = [2, 4, 5, 6, 12, 3, -1]
i = findBitonic(a)
# binarySearch(a[i:])
# searchRight(a[:i])
