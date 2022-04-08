#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def f(x):
    return -(((-(np.square(x)))/10)+(3*x))

varbound=np.array([[0,31]]*1)
model=ga(function=f, dimension=1, variable_type='int', variable_boundaries=varbound)
model.run()

