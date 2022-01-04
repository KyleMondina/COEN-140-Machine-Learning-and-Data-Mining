#!/usr/bin/env python
# coding: utf-8

# In[3]:


###Question 2 a
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from pdb import set_trace as st


### p(x|0) versus x for 0=1
theta1 = 1
x1 = np.linspace(-8,8,50)
expo1 = expon.pdf(x1,theta1)

plt.title('p(x|0) versus x for 0=1')
plt.grid(which='both',axis='both', color='grey',linestyle=':')
plt.plot(x1,expo1,label='p(x|0)',color="tab:blue",linewidth=3)
plt.show()


### p(x|0) versus 0 for x = 2
theta2 = np.linspace(0,5,20)
x2 = 2
expo2 = expon.pdf(x2,theta2)


plt.title('p(x|0) versus 0 for x=2')
plt.grid(which='both',axis='both', color='grey',linestyle=':')
plt.plot(theta2,expo2,label='p(x|0)',color="tab:blue",linewidth=3)
plt.show()

