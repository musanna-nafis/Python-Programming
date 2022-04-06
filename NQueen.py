#!/usr/bin/env python
# coding: utf-8

# In[ ]:


grid=int(input("Enter Grid:"))
print("");

board = [[0 for i in range(grid)] for j in range(grid)]
print("Initial Grid")
print(" ")
for i in range(grid):
    for j in range(grid):
        print(board[i][j],end = '')
        print(" ",end = '') 
    print("")

    
    
def Solv(board,column):
    
    if column >= grid:
        return True

    for i in range(grid):
        if (Ok(board,i,column))==True:
            board[i][column]=1
            if (Solv(board,column+1))==True:
                return True
            board[i][column]=0
    return False



def Ok(board,row,column):
    for i in range(column):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1),
                    range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, grid, 1),
                    range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True



Solv(board, 0)
print(" ")
print("Final grid after placing N queen")
print(" ")
for i in range(grid):
    for j in range(grid):
        print(board[i][j],end = '')
        print(" ",end = '')
        
    
    print("");

