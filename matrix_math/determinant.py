#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def determinant(matrix):
    coff = cofactor_mat(matrix)
    determ = 0
    for i in matrix :
        for j in i :
            i_index = matrix.index(i)
            j_index = i.index(j)
            part = matrix[i_index][j_index]*coff[i_index][j_index]
            determ += part
    return determ

