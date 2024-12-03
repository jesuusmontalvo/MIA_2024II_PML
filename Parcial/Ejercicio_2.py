import Ejercicio_1 as e1
import numpy as np

def propagate(p0, k, tm):
    return p0*tm**k 

p0 = np.zeros(10)
p0[0] = 1

propagate(p0, 30, e1.transition_matrix(10))