n =input().split(" ")
a=sorted(n)
x=[]
for i in a:
    if i not in x:
        x.append(i)
s=sorted(x)
print(s[-2])
        