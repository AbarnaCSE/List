def triplets(list,n,sum):
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(list[i]+list[j]+list[k]==sum):
                    print(list[i]," ",list[j]," ",list[k],sep =" ")
list = [10,20,30,9]
n = len(list)
triplets(list,n,59)                    
