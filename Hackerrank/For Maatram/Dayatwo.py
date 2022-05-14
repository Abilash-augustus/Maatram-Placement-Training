from itertools import product
from posixpath import split


N=int(input("Enter the number of array elements : "))
A = []
i = 0
while i<N:
    a=int(input())
    A.append(a)
    i+=1
print(A)
x=sum(A)
product=1

for y in A:
    product = product*y

if x%2==0:
    print("Sum of the array elements in ",x)
else:
    print("Sum of the prducts = ", product)
    
    
    




