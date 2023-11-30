def mangoes(values):
    low = min(values)
    high = max(values)
    if high - low <= 1:
        print(list)
        return list(values)
    s = sum(values)
    n = len(values)
    avg = s//n
    result = [avg] *n
    for i in range (s % n):
        result[i] += 1
    return result
values = []
m = int(input("Enter number of students:"))
for i in range(0,m):
    element = int(input("Number of Mangoes in bag:"))
    values.append(element)
print(values)    
print(mangoes(values))    