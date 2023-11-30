def sublist(list, N):
    sum = 0
    s = set()
    for i in range(N):
        sum += list[i]
        if sum == 0 or sum in s:
            return True
        s.add(sum)
    return False
list = [4,2,-3,1,6]
N = len(list)  
if sublist(list, N) == True:
    print("Found a subarray with 0 sum")
else:
    print("No Such sub array exits!")