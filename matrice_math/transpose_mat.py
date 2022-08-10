#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def transpose_mat(matrix) :
    new_mat_i = []
    new_mat = []
    ilen = len(matrix)
    jlen = len(matrix[1])
    count = 1
    for i in matrix :
        i_index = matrix.index(i)
    #     print(i)
        for j in i :
    #         print(j, end = " ")
            j_index = i.index(j)
    #         print(j_index, end = " ")
            new_mat_i.append(matrix[j_index][i_index])
    #         print(j_index, i_index, end = " ")
    #         print(new_mat_i)
            if count == ilen:
                count = 0
                new_mat.append(new_mat_i)
                new_mat_i = []
            count+=1
    return new_mat

