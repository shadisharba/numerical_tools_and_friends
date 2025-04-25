# [sympy](https://docs.sympy.org/latest/index.html)
# Jacobian https://docs.sympy.org/latest/modules/matrices/matrices.html

from sympy import sin, cos, Matrix
from sympy import MatrixSymbol, Matrix, diff
from sympy.abc import rho, phi
from sympy.vector import CoordSys3D
from sympy.abc import a, b, c
from sympy import sin, cos, trigsimp, diff

X = Matrix([rho * cos(phi), rho * sin(phi), rho**2])
Y = Matrix([rho, phi])
X.jacobian(Y)

X = Matrix([rho * cos(phi), rho * sin(phi)])
X.jacobian(Y)

X = MatrixSymbol('X', 3, 3)
Y = MatrixSymbol('Y', 3, 3)
Z = (X.T * X).I * Y

Z = (X.T * Y) * X
Z.diff(X).simplify()

from sympy import derive_by_array
derive_by_array(Z, X)

n = 5
A = MatrixSymbol("A", n, n)
x = MatrixSymbol("x", n, 1)
diff(A.T * x, x)

# https://github.com/sympy/sympy/issues/5858
x = MatrixSymbol("x", n, n)
diff(A.T * x, x)


g = Function('g')(s, b)
diff(g, s)

N = CoordSys3D('N')

v = (a * b + a * c + b**2 + b * c) * N.i + N.j
print(v)
# diff(v.norm(), a)