a=input()
while a[-1]==0:
    a=a[:-1]
n=int(a)
y = str(abs(n))
y = y.strip()
y = y[::-1]
output = int(y)
if output >= 2** 31 -1 and output <= -2** 31:
    print(0)
elif n < 0:
    x= -1 * output
    print(x)
elif a[0]=="+":
    print(a[0]+y)
else:
    print(output)
