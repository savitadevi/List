n=int(input("enter any number="))
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print("perfeect number",n)
else:
    print("not perfect number",n)
    