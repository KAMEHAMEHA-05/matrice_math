#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def adjoint_mat(matrix) :
    coff = cofactor_mat(matrix)
    adjoint = transpose_mat(coff)
    return adjoint

