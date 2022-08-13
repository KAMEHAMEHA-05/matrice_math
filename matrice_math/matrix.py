#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[5]:


def subtract(m1, m2):
    m3 = []
    for i in m1 :
        part = []
        for j in i :
            i_index = m1.index(i)
            j_index = i.index(j)
            part.append(j-m2[i_index][j_index])
        m3.append(part)
    return m3


# In[12]:


def scalar_mult(num, mat) :
    new_mat = []
    for i in mat :
        part = []
        for j in i :
            part.append(num*j)
        new_mat.append(part)
    return new_mat


# In[16]:


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


# In[ ]:


def transpose(matrix) :
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


# In[ ]:


def adjoint(matrix) :
    coff = cofactor_mat(matrix)
    adjacent = transpose_mat(coff)
    return adjacent


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


# In[ ]:


def inverse(matrix):
    ilen = len(matrix)
    inv_mat_i = []
    inv_mat = []
    determ = determinant(matrix)
    if int(determ) == 0:
        print('No inverse exists, as determinant is equal to 0')
    else :
        adj = adjacent_mat(matrix)
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


# In[ ]:


def minor_mat(matrix) :
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
            coff = (work[0][0]*work[1][1]-work[0][1]*work[1][0])
            coff_m_i.append(coff)
            if count == ilen:
                count = 0
                coff_m.append(coff_m_i)
                coff_m_i = []
            count+=1
    return coff_m


# In[ ]:


def minor(matrix,i, j) :
    mat = minor_mat(matrix)
    mino = mat[i][j]


# In[ ]:


def cofactor(matrix, i, j) :
    mat = cofactor_mat(matrix)
    mino = mat[i][j]

