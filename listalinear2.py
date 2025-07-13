# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:21:36 2019

@author: paulo
"""
from copy import copy;
import numpy as np;
from fractions import Fraction

mat = np.matrix(np.arange(20).reshape(4,5));

mat=mat.astype("object");

mat[0][0]=[1.0, 2.0, -1.0, 0.0, -4.0];
mat[1][0]= [Fraction(0, 1) ,Fraction(-1, 1), Fraction(1, 1), Fraction(-1, 1),
  Fraction(0, 1)];
mat[2][0]= [Fraction(0, 1) ,Fraction(0, 1), Fraction(5, 1), Fraction(-1, 1),
  Fraction(-1, 1)];
mat[3][0]= [Fraction(0, 1) ,Fraction(0, 1), Fraction(0, 1), Fraction(29, 5),
  Fraction(29, 5)];

submat = np.array(mat[:, :4], dtype=float)

det = np.linalg.det(submat)
print (det);