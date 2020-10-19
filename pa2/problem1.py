# given a swet of points on a plane find all the maximal points (no points above or to the right)

import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def checkPoint(p_array):
    count = 0
    n = len(p_array)
    for i in range(n):
        cand = p_array[i]
        if isMaximal(cand, p_array):
            count += 1
    return count

def isMaximal(cand, p):
    for k in range(len(p)-1):
        check = p[k]
        if cand.x < check.x and cand.y < check.y:
            return False
    return True

def sortPoints(p_array):
    n = len(p_array)
    # implement merge sort on points x value.
    if n > 1:
        m = n//2
        left = p_array[:m]
        right = p_array[m:]
        left = sortPoints(left)
        right = sortPoints(right)

        # merge part
        p_array = []
        while len(left) > 0 and len(right) > 0:
            if left[0].x < right[0].x:
                p_array.append(left[0])
                left.pop(0)
            else:
                p_array.append(right[0])
                right.pop(0)

        for k in left:
            p_array.append(k)
        for k in right:
            p_array.append(k)

    return p_array

# we will take our sorted array and walk through backwords looking for Y values larger than current index.
def getMaximal(sorted_array):
    count = 1
    i = len(sorted_array) - 1
    cand = i
    while i >= 0:
        if sorted_array[i].y > sorted_array[cand].y:
            cand = i
            count += 1
        i -= 1
    return count



#### DRIVER CODE ######
p = []
z = range(7)
for i in z:
    x = random.randint(-10, 10)
    y = random.randint(-10,10)
    p.append(Point(x,y))
    print(x,y)

# this function sorts the list in order of x
m = sortPoints(p)
count = getMaximal(m)

# l =checkPoint(p)
print(count)











