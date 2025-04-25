# https://github.com/aztennenbaum/symbolic-mat-diff
# https://zulko.wordpress.com/2012/04/15/symbolic-matrix-differentiation-with-sympy/

from symbolic_mat_diff.symbdiff import diff as sym
a = sym.MatrixSymbol('a', 5, 1)
print(sym.matDiff(sym.Transpose(a) * a, a))

X = sym.MatrixSymbol('X', 5, 5)
print(sym.matDiff(sym.Transpose(a) * X * a, X))
