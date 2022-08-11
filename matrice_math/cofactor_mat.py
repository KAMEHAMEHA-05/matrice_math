#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cofactor_mat(matrix) :
    from copy import deepcopy
#     matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ilen = len(matrix)
    work = deepcopy(matrix)
    coff_m = []
    coff_m_i = []
    coff = 1
    count = 1
    for i in matrix :
        work = deepcopy(matrix)
        for j in i :
            work = deepcopy(matrix)
            i_index = matrix.index(i)
            j_index = i.index(j)
            work.pop(i_index)
            for p in work :
                p.pop(j_index)
            power = i_index+j_index+2
            ind_str = ('-1'+'*(-1)'*power+'/(-1)')
            ind = eval(ind_str)
            coff = ind*(work[0][0]*work[1][1]-work[0][1]*work[1][0])
            coff_m_i.append(coff)
            if count == ilen:
                count = 0
                coff_m.append(coff_m_i)
                coff_m_i = []
            count+=1
    return coff_m

