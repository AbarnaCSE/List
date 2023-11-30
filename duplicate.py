def duplicate(list1,list2,list3):
    result =[]
    for i in list1:
        if i in list2 and i in list3:
            result.append(i)
    print(list(set(result)))
list1 =[10,20,68,52]
list2 =[20,30,50,20]
list3 =[10,20,68,52]
common = duplicate(list1,list2,list3)


       
       
