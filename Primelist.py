Prime = [10,501,22,37,100,999,87,351]
for x in Prime:
   for i in range (2,x):
      if x%i==0:
         Prime.remove(x)
      else:
         break
print(Prime)         

