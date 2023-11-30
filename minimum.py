def element(list, N):
    minimum = list[0]
    for i in range(N) :
        if list[i] < minimum :
            minimum = list[i]
    return minimum
list = [5, 6, 1, 2, 3, 4]
N = len(list) 
print(element(list,N))