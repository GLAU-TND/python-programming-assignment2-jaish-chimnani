from itertools import permutations 
a=list(map(int,input().split()))
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)):
        lst.append("".join(map(str,i)))  
    return max(lst) 
  
print(largest(a)) 
  
