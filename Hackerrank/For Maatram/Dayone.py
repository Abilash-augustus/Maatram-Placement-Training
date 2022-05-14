


x=int(input("Enter the number X"))
y=int(input("Enter the number Y"))
p=int(input("Enter the number p"))
q=int(input("Enter the number q"))


listx= []
listy= []


for i in range(p,q+1):
    if i%x==0:
       listx.append(i)
print(listx)

for j in range(p,q+1):
    if j%y==0:
       listy.append(j)
print(listy)

a = sum(listx)
b = sum(listy)

print("x-multiples-Count = ",len(listx))

print("y-multiples-Count = ",len(listy))

print("x-multiples-Sum = ",a)

print("x-multiples-Sum = ",b)

if a>b:
    print("Difference-in-Sum",a-b)
else:
    print("Difference-in-Sum",b-a)
