#  lis=["a","b","a","c","b","c","a","a"]
#  i=0
#  a=[]
 
#  while i<len(lis):
#      count=0
#      j=0
#      while j<len(lis):
#          if lis[i]==lis[j]:
#              b.append(lis[i])
#             count=count+1
#         j+=1 
#      b.append(count)
#     b.append(lis[i])    
#     if b not in a:
#          a.append(b)           
#     i+=1
# print(a)
lis=["a","b","a","c","b"]
i=0
a=[]
b=[]
count=0
count=0
while i<len(lis):
    if lis[i]not in a:
        a.append(lis[i])
        count=count+1
    else:
        b.append(lis[i])
        count=count+1
        
    i=i+1
print(a,)
print(count)
       


    
   













     