list=[15,20,21,91,90,65,185,25,81]
more_then50=[]
i=0
b=[]
while i<len(list):
  if list[i]%5==0:
    b.append(list[i])
  if list[i]>50:
    more_then50.append(list[i])
  i+=1
print(b)