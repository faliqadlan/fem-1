from sympy import symbols, integrate, Eq
import numpy as np

# Definisikan simbol
x = symbols("x")
j_max = 4
q = symbols("q1:%d" % j_max)

# Definisikan persamaan
R = -1
for j in range(1, j_max):
    R += q[j - 1] * (j * x ** (j - 1) - x**j)

intRArr = []

for i in range(1, j_max):
    intR = (x ** (i - 1)) * R
    integrated_R = integrate(intR, (x, 0, 1))
    intRArr.append(integrated_R)




# # Buat matriks dari array intRArr
# A = Matrix(np.array(intRArr).reshape(-1, j_max - 1))

# print(A)

# b = Matrix([1, 1 / 2, 1 / 3])

# print(b)

# # Selesaikan sistem persamaan linear
# solution = linsolve((A, b), q)

# print(solution)
