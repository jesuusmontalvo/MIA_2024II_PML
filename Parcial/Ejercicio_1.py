import numpy as np
from matplotlib import pyplot as plt


def transition_matrix(n):
    m = n - 1
    matriz_transicion = np.zeros((n,n))
    matriz_transicion[0,:n] = 0.2 * np.ones((1,n))
    matriz_transicion[m,m] = 1
    np.fill_diagonal(matriz_transicion[1:,:m], [0.8] * m)
    return matriz_transicion
##############################3
def propagate(p0, k, tm):
    return np.linalg.matrix_power(tm, k) @ p0 

tm = transition_matrix(10)
p0 = np.zeros(10)
p0[0] = 1
pk = propagate(p0, 30, tm)

# print(pk.shape)
####################
tm = transition_matrix(10)
p0 = np.zeros(10)
p0[0] = 1

estados = np.arange(10)
for k in range(1,11):
    plt.plot(estados, propagate(p0, k, tm))

plt.title("Estado vs Distribución de Probabilidad")
plt.xlabel("Estado")
plt.ylabel("Distribución de probabilidad")
plt.savefig("qsn3.png")
plt.show()
