def firstnonrepeating(List,n):
    for i in range(n):
        j=0
        while(j<n):
            if(i != j and List[i]==List[j]):
                break
            j+=1
        if(j == n):
            return List[i]
    return -1
List = [10,501,10,37,100,999,87,351]
n = len(List)
print(firstnonrepeating(List,n))        