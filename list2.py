# list=[7,4,[3,40,[17,19,[14,86]],78]]
# print(len(list))
# print(list[2][2][2][1])
# print(list[2][2][1])


# list=[2,3,[4,5,6,[7,8,9,[10]],11,12]]
# print(list[2][2])
# print(list[2][3][0])
# print(list[2][3][3][0])
# print(list[2][4])

# list=[8,9,10,[18,10,5,[11],[10]],1,2,3]
# print(list[6])
# print(list[3][4][0])
               

# list=[20,10,[12,14,18,10],[11,12,20],[4,5,6,[8,9,10,11]],10,8,7]  
# print(len(list))
# print(list[4][3][2])
# print(list[6])

# list=[1,2,[3,4,[5,6,[8,9]],10,11,12],[13,14,15],16,17,18]
# print(len(list))
# print(list[2][2][2][1])
# print(list[2][3])
# print(list[5])

# i=0
# while i<=5:
#     j=0
#     while j<=4:
#         if j==0 or i==5:
#             print("*",end="")
#         else:
#             print("",end="")
#         j=j+1
#     print()
#     i=i+1
        


# i=0
# while i<=4:
#     j=0
#     while j<=i:
#         if j==0 or i==4:
#             print("*",end="")
#         else:    
#             print("",end="")
#         j=j+1
#     print()
#     i=i+1           


# a=[7,[3,8,[9,[18,4],81],78],6]
# print(a[1][1])
# print(a[1][2][1][1])
# print(a[1][2][0])
# print(a[1][3])
# print(a[2])

list=[12,3,4]
min=len(list)
i=0
while i<len(list):
    if list[i]<min:
        min=list[i]
    i=i+1
print(min)        

