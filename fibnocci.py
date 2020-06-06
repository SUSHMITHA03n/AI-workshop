#!/usr/bin/env python
# coding: utf-8

# In[18]:


def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input())
fib(n)


# In[ ]:







# In[ ]:


6

