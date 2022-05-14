
X=int(input())
print(X)
N=list(map(int,input().split()))
for i in N:
    if N.count(i)==1:
        print(i,end=" ")