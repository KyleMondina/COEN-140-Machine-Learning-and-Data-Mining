#!/usr/bin/env python
# coding: utf-8

# In[6]:



get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from pdb import set_trace as st


### p(x|0) versus x for 0=1

x = np.linspace(-2,2,50)

s0 = 2*(1-x)
s1 = 2*x


plt.grid(which='both',axis='both', color='grey',linestyle=':')
plt.plot(x,s0,label='s0',color="tab:blue",linewidth=3)
plt.plot(x,s1,label='s1',color="tab:green",linewidth=3)
plt.show()

