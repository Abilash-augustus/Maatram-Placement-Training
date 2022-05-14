l=[]
N=int(input())
for i in range(0,N):
    s=input().split()
    for x in s:
        if "#" in x:
           l.append(x)
a=[]
x=[]
count=0
l=sorted(l)

for y in l:
    ans=(y,l.count(y))
    x.append(ans)

for i in x:
    if i not in a:
        a.append(i)
        
def counter(s):
    return s[-1]

pre_final=sorted(a,key=counter,reverse=True)

pre_final=pre_final[0:5]

for i in pre_final:
    print(i[0])





