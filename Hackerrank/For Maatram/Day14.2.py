'''
column_length=len(column_name)
print(column_name, column_length)

if column_length==2:
    x=ord(column_name[0])
    y=int(x)-16
    print(ord(str(y)))'''

column_name=input()
result = 0
for i in range(len(column_name)):
    result = result * 26
    result = result + ord(column_name[i]) - ord('A') + 1
print(result)
 

