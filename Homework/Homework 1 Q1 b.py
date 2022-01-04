#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon
from pdb import set_trace as st


x = np.linspace(-6, 6, 5000)
# x1 and x2 denote p(x|w_1) and p(x|w_2)
x1 = norm.pdf(x, 0,1)  
x2 = norm.pdf(x, 1,1.41) 


plt.grid(which='both',axis='both', color='grey',linestyle=':')
plt.plot(x, x1, label='p(x|W1)', color='tab:blue', linewidth=3)
plt.plot(x, x2, label='p(x|W2)', color='tab:green', linewidth=3)
plt.title('Class-conditional Density (Likelihood)')
plt.legend(fancybox=True, framealpha=0.5, fontsize=18)

intersections = [0.84018,-2.84]
plt.axvline(x=0.84,color='gray',linestyle='--')
plt.axvline(x=-2.84018867541,color='gray',linestyle='--')

plt.show()

