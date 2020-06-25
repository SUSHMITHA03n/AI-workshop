n=int(input())
a=list(map(int,input(" x = ").strip().split()))[:n]
print(a)
element = 5 
beforeElement = 6
index = a.index(beforeElement)  
a.insert(index, element)  
print(a) 


