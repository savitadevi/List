list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
b=[]
while i<len(list):
    j=0
    a=[]
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
    print(count)
    a.append(count)    
    a.append(list[i])
    if a not in b:
        b.append(a)
    i=i+1
print(b)
