#!/usr/bin/env python
# coding: utf-8

# ## Numerical Computing with Python, Part 3:   Numerical Modeling  <a class="tocSkip">
#     
# To start, let's do a bit of symbolic math to get the gears churning...

# In[1]:


import sympy
sympy.init_printing()


# In[2]:


x = sympy.Symbol('x')


# In[3]:


x


# In[4]:


x**2


# In[5]:


expr = x**4 + x**3 + x**2 + x + 1


# In[6]:


expr


# In[7]:


expr.diff(x)


# In[8]:


expr.diff(x,3)


# In[9]:


expr.diff(x,3).expand()


# In[10]:


expr.integrate(x)


# In[11]:


expr.integrate((x,0,3))


# In[12]:


sympy.integrate(expr,x)


# In[13]:


sympy.integrate(expr,(x,0,3))


# In[14]:


sympy.cos(x)


# In[15]:


sympy.cos(x).series(x,n=10)


# In[16]:


sympy.cos(x).integrate(x)


# In[17]:


sympy.tan(x)


# In[18]:


sympy.tan(x).integrate(x)


# In[19]:


n = sympy.symbols("n")


# In[20]:


from sympy import oo


# In[21]:


x = sympy.Sum(1/(n**2), (n, 1, oo))


# In[22]:


x


# In[23]:


x = sympy.Symbol('x')


# In[24]:


a = sympy.Sum(x**n/(sympy.factorial(n)), (n, 0, oo))


# In[25]:


a


# In[26]:


a.doit()


# In[27]:


sympy.Matrix([1,2])


# In[28]:


import numpy as np


# In[29]:


b = np.array([[1,2],[3,4]])


# In[30]:


b


# In[31]:


m = sympy.Matrix(b)


# In[32]:


m


# In[33]:


type(m)

