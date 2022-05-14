str=input()
count=0
for i in range(len(str)+1):
    if str[i]!=str[i+1]:
        count+=1
        i=i+1
print(count)