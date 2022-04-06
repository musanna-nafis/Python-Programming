#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
def minimax(depth,nodeIndex,maxormin,values,alpha,beta):

    if depth == 3:
        return values[nodeIndex]

    if maxormin:
        maxi=-math.inf
        for i in range(0, 2):
            val = minimax(depth+1,(nodeIndex*2+i),False,values,alpha,beta)
            maxi = max(maxi, val)
            alpha = max(alpha, maxi)
            if beta <= alpha:
                break

        return maxi

    else:
        maxi=math.inf
        for i in range(0, 2):
            val = minimax(depth+1,(nodeIndex*2+i),True,values,alpha,beta)
            maxi = min(maxi, val)
            beta = min(beta,maxi)

            if beta <= alpha:
                break

        return maxi




values = [3, 5, 6, 9, 1, 2, 0, -1]   
print("The optimal value is :", minimax(0, 0, True, values, -10000, 10000))

