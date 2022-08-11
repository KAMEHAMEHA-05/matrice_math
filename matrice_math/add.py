#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(m1, m2) :
    m3 = []
    for i in m1 :
        part = []
        for j in i :
            i_index = m1.index(i)
            j_index = i.index(j)
            part.append(j+m2[i_index][j_index])
        m3.append(part)
    return m3

