#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def matrix_mult(m1, m2) :
    count = 1
    new_mat = []
    mult_a = []
    mult = []
    item = 0
    jlen = len(m2[0])
    for i in m1 :
        for y in m2[m1.index(i)]:
            for x in m2 :
                new_mat.append(x[m2[m1.index(i)].index(y)])
            for j in i :
                j_index = i.index(j)
                item_a = j*new_mat[j_index]
                item += item_a
            new_mat = []
            mult_a.append(item)
            item = 0
            if count == jlen :
                mult.append(mult_a)
                mult_a = []
                count = 0
            count+=1
    return mult

