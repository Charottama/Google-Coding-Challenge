#!/usr/bin/env python
# coding: utf-8

# In[1]:


def primerization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
            #print ('a', n, i)
        else:
            n //= i
            #print ('b', n)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


# In[2]:


def solve(n, p):
    prime = primerization(n)
    while len(prime) >= p:
        n -= prime[p-1]
        prime = primerization(n)
    
    return n


# In[3]:


#def solve (n, p):
#    # Type your code here
#    return n

T = int(input())
for _ in range(T):
    n = int(input())
    p = int(input())
    
    out_ = solve(n, p)
    print(out_)


# In[ ]:




