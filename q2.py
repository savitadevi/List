list=[1,0,1,0]
a=0
i=-1
sum=0
while i>=(-len(list)):
    sum=sum+(list[i]*2**a)
    a=a+1
    i=i-1
print(sum)