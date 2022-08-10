#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def scalar_mult(num, mat) :
    new_mat = []
    for i in mat :
        part = []
        for j in i :
            part.append(num*j)
        new_mat.append(part)
    return new_mat

