#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inversion=0
blankTile=0
dimension = int(input("Enter Dimension:"))

puzzle=[]
print("Enter the entries rowwise:")

for i in range(dimension):
    a =[]
    for j in range(dimension):      
         a.append(int(input()))
    puzzle.append(a)
    

numbers = [0 for i in range((dimension*dimension)-1)]
for i in range ((dimension*dimension)-1):
    numbers[i]=i+1

for i in range(dimension):
    for j in range(dimension):
        if puzzle[i][j]==0:
            blankTile=i
        total=puzzle[i][j]
        numbers[total-1]=0;
        for k in range(total-1):
            if numbers[k]!=0:
                inversion=inversion+1
                

blankTile=dimension-blankTile

print("Number of inversion:")
print(inversion)
if dimension%2!=0 and inversion%2==0:
    print("solvable")
elif dimension%2==0 and blankTile%2!=0 and inversion%2==0:
     print("solvable")
elif dimension%2==0 and blankTile%2==0 and inversion%2!=0:
    print("solvable")
else:
    print("Not Solvable")

