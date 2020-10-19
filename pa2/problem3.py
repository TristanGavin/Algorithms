# given an array find the max number of oscilations (larger number, smaller number, larger number...)

def oscolate(array):
    streak = 1
    curStreak = 0
    high = True
    for n in range(1,len(array)):
        if n == 1:
            if array[n] > array[n-1]:
                high = True
                curStreak += 1
            else:
                high = False
                curStreak += 1
        elif high:
            if array[n] < array[n-1]:
                curStreak +=1
                high = False
                if curStreak > streak:
                    streak = curStreak
            else:
                curStreak = 1
        else:
            if array[n] > array[n-1]:
                curStreak += 1
                high = True
                if curStreak > streak:
                    streak = curStreak
            else:
                curStreak = 1
    return streak
    
# Driver Code
a = [2, 3, 5, 2, 5, 1, -2]
streak = oscolate(a)
print(streak)
