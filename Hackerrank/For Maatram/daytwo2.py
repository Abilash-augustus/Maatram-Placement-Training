n=input("Enter the unformated phone number : ")
PN = []
l1=[]
for i in n:
    if i.isnumeric():
        PN.append(i)
print(PN)
s=len(PN)

for x in range(0,PN):