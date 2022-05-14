a=input().split()
b=len(a[-1])
c=""
for i in a[-1]:
    if i.isalpha():
        c+=i
print(len(c))