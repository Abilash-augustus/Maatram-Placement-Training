n=int(input())
if n==1:
    print("true")
else:
    while(n>4):
        n=n/4
    if n%4==0:
        print("true")
    else:
        print("false")
 