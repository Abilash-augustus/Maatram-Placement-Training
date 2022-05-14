t = input("Enter")
count = 0
for i in range(len(t)-1):
    if t[i]!=t[i+1]:
        count+=1
print(count+1)