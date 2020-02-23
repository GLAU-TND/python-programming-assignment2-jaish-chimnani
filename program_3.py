x=int(input())
count = 0
while (x!=0): 
    x = (x & (x << 1)) 
    count=count+1
print(count)

