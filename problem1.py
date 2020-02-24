a=eval(input())
b=len(str(max(a)))
m=0
res=''
c=[]
print(a)
a=[str(i) for i in a]
for h in range(len(a)):
    m=0
    for i in a:
        for j in a:
            if i!=j and i not in c:
                y=i+j
                u=int(y[:k])
                if y>m:
                    n=str(i)
    c.append(n)
for i in c:
    res=res+i
print(res)
