import numpy as np
import sys

arq = open('matriz1.txt', 'r')
matriz = arq.readlines()
arq.close()
m = []
for i in range(len(matriz)):
    m.append(matriz[i].split())
m = np.array(m, dtype=float)
print(m, '\n')

arq = open('resultado_matriz.txt', 'w')
arq.write(str(m)+'\n\n')
tamanho = np.shape(m)
linhas = tamanho[0]
colunas = tamanho[1]

print(' Gauss elimina a parte de baixo ')
coeficiente = 0
for i in range(0, linhas, 1):
    pivor = m[i, i]
    caminhar = i + 1
    for k in range(caminhar, linhas, 1):
        if np.abs(m[k, i]) >= 0:
            if np.abs(m[i, i]) == 0:
                if np.abs(m[k, i]) != 0:
                    aux = np.copy(m[k, :])
                    m[k, :] = np.copy(m[i, :])
                    m[i, :] = np.copy(aux)
                    m[i, :] = m[i, :] / m[i, i]
                    pivor = m[i, i]
                    print(m, '\n')
                    arq.write(str(m)+'\n\n')
                else:
                    if np.abs(m[k + 1, i]) != 0:
                        aux = np.copy(m[k + 1, :])
                        m[k + 1, :] = np.copy(m[i, :])
                        m[i, :] = np.copy(aux)
                        print(m, '\n')
                        arq.write(str(m)+'\n\n')
                        m[i, :] = m[i, :] / m[i, i]
                        pivor = m[i, i]
                        print(m, '\n')
                        arq.write(str(m)+'\n\n')
                    else:
                        print("Essa matriz não pode ser resolvida pelo metodo Gauss_Jordan")
                        sys.exit()
            else:
                if np.abs(m[k, i]) != 0:
                    coeficiente = pivor / m[k, i]  # multiplicador
                    m[k, :] = m[k, :] * coeficiente - m[i, :]
        else:
            coeficiente = 'divisao por zero'
        print('coeficiente: ', coeficiente)
        print(m, '\n')
        arq.write(str(m)+'\n\n')

print('  Gauss-Jordan eliminar a parte de cima  ')
ultfila = linhas - 1
ultcoluna = colunas - 1
for i in range(ultfila, 0 - 1, -1):
    for d in range(0, linhas, 1):
        if np.any(m[d, :ultcoluna]) == 0:
            print("Essa matriz não tem solução")
            sys.exit()

    # Normaliza o 1 elemento diagonal
    m[i, :] = m[i, :] / m[i, i]
    pivor = m[i, i]
    # acima da linha i
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        if np.abs(m[k, i]) > 0:
            coeficiente = pivor / m[k, i]
            m[k, :] = m[k, :] * coeficiente - m[i, :]
        else:
            coeficiente = 'Divisão por zero.'
        print('coeficiente: ', coeficiente)
        print(m, '\n')
        arq.write(str(m)+'\n\n')
X = m[:, ultcoluna]
X = np.transpose([X])
# R = ['X = {:.1f}'.format(float(X[0])), 'Y = {:.1f}'.format(float(X[1])), 'Z = {:.1f}'.format(float(X[2]))]
# R = np.transpose([R])
print('Matriz final: ')
print(m, '\n')
arq.write(str(m)+'\n\n')
for e in X:
    e = '[%.2f]' % (float(e))
    print(e)
    arq.write(str(e)+'\n')
arq.close()
