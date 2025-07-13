# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 23:10:16 2019
@author: paulo.sergio
"""
from copy import copy;
import numpy as np;
from fractions import Fraction;

filere = open("matriz.txt","r");
matriz=[];
line=filere.readlines();
for i in range(len(line)):
    matriz.append(line[i].split());
    
mat=np.array(matriz);

mat=mat.astype("float");
det= copy(mat[:, 0:len(mat)]);
mat=mat.astype("object");

filewr= open("matrizresolvida.txt","w");
filewr.write("matriz >"+str(mat)+"\n");
filewr.write(" \n");

pivo=0;
lp=0;
l=True;
j=0;

if(np.linalg.det(det)!=0):
    for i in range(0,len(mat)):
        pivoj=0;
        pivo=mat[i,i];
        if(pivo==0):
            l=True;
            
        while(l):
            pivo=mat[i,i];
            if(pivo==0):
                filewr.write("pivo > "+str(pivo)+"\n");  
                filewr.write(" \n");
                if(j!=len(mat)):
                    filewr.write("matriz > "+str(mat[j,0])+"\n");
                    filewr.write(" \n");
                    if(mat[j,0]!=0):
                        aux = copy(mat[i][0]);
                        mat[i][0]=mat[j][0];    
                        mat[j][0]=aux
                    j=j+1; 
                filewr.write("matriz >"+str(mat)+"\n");
                
            else:
                l=False;
                
        lp=i;
        filewr.write("pivo > "+str(pivo)+" \n");
        filewr.write(" \n");
    
        for i in range(i+1,len(mat)):
            filewr.write("aplicando a formula >"+str(mat[i])+" = "+str(mat[i])+" - "+str(mat[i])+" / "+str(pivoj)+" * "+str(mat[lp])+"\n");
            filewr.write(" \n");
            pivoj=Fraction(mat[i,lp]/pivo);
            for j in range(0,len(mat)+1):
                mat[i,j]=Fraction(mat[i,j])-Fraction(pivoj)*Fraction(mat[lp,j]);
    
        filewr.write("matriz >"+str(mat)+"\n");
    
    
    for i in range(len(mat)-1,-1,-1):
        if(len(mat)-1==i):
            mat[i,len(mat)]=mat[i,len(mat)]/mat[i,i];
            mat[i,i]=mat[i,i]*0;
            mat[:,len(mat)-1]=mat[:,len(mat)-1]*mat[i,len(mat)]
    
        for j in range(len(mat)-1,-1,-1):
            if(j!=i):
                mat[i,len(mat)]=mat[i,len(mat)]-mat[i,j];
                mat[i,j]=mat[i,j]*0;
            if(j==i and mat[i,i]!=0 ):
                mat[i,len(mat)]=mat[i,len(mat)]/mat[i,i];
                mat[i,i]=mat[i,i]*0;
                mat[:,i]=mat[:,i]*mat[i,len(mat)];
    
    for i in range(0,len(mat)):            
        filewr.write("Resposta da linha "+str(i+1)+" > "+str(mat[i,len(mat)])+"\n");
else:
    filewr.write("Sistema Possível e Indeterminado ou Sistema Impossível\n");
filewr.write(" \n");
filere.close;
filewr.close;