#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def inverse_mat(matrix):
    ilen = len(matrix)
    inv_mat_i = []
    inv_mat = []
    determ = determinant(matrix)
    if int(determ) == 0:
        print('No inverse exists, as determinant is equal to 0')
    else :
        adj = adjoint_mat(matrix)
        part_a = 1/determ
        count = 1
        for i in adj :
            for j in i :
                i_index = adj.index(i)
                j_index = i.index(j)
                item = part_a*adj[i_index][j_index]
                inv_mat_i.append(item)
                item = 1
                if count == ilen:
                    count = 0
                    inv_mat.append(inv_mat_i)
                    inv_mat_i = []
                count+=1
        return inv_mat

