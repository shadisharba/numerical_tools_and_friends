from __future__ import print_function
from sympy import *

init_printing(use_unicode=True)

dt = symbols('dt')

# yield functions and viscous parameters
f_p, f_d, dg_p, dg_d, kp, np, kd, nd = symbols('f_{p}, f_{d}, \\lambda_{p}, \\lambda_{d}, k_{p}, n_{p}, k_{d}, n_{d}', real=true)

# dual variables and related parameters
s, b, d, Y, Y0, a, c, sy = symbols('\\sigma, \\beta, D, Y, Y_0, a, c, \\sigma_{y}', real=true)

# misc
Id, T, C, epse_t, N, b_tr, d_tr = symbols('I^{D}, \\tau^{D}, C, \\varepsilon_{t}, N, \\beta_{t}, D_{t}', real=true)

# stress-like term
T = s * Id - b

# yield functions
f_p = Function('f_p')(s, b, d)
f_d = Y - Y0

# plastic deviatoric flow vector
N = Function('N')(s, b, d)

A1 = dg_p - kp * f_p**np * dt
# there are macaulay brackets here
A2 = dg_d - kd * f_d**nd * dt
# there are macaulay brackets here
A3 = s - (1 - d) * C * (epse_t - dg_p * N)
A4 = b - b_tr - dg_p * (c * N - a * b)
A5 = d - d_tr - dg_d
A6 = Y - 0.5 * C * (epse_t - dg_p * N)**2

# NOTE: If we wanted to do CSE (common subexpression) that's done with this line of code
# (simplify(cse(diff(T/abs(T),s)))).subs(substitution_list)
substitution_list = {
    sqrt(3 / 2): '\\sqrt{\\frac{3}{2}}',
    T: 'T',
    sign(T): '\\frac{\\tau}{\\lVert(\\tau)\\rVert}',
    -d + 1: '(1-D)',
    1.0 * C: 'C'
}

# print('\\begin{center}')
# for a in {A1,A2}:
#     print('************\\\\')
#     print('\\begin{align*}')
#     print(latex(simplify(Derivative(a, dg_p).doit().subs(substitution_list))), '\\\\')
#     print(latex(simplify(Derivative(a, dg_d).doit().subs(substitution_list))), '\\\\')
#     print(latex(simplify(Derivative(a, s).doit().subs(substitution_list))), '\\\\')
#     print(latex(simplify(Derivative(a, b).doit().subs(substitution_list))), '\\\\')
#     print(latex(simplify(Derivative(a, d).doit().subs(substitution_list))), '\\\\')
#     print(latex(simplify(Derivative(a, Y).doit().subs(substitution_list))), '\\\\')
#     print('\end{align*}')
# print('\\begin{center}')

# f_p = (sqrt(3/2)*Abs(T)/(1-d)+ a/(2*c) * b**2 - sy)
# # substitution_list[diff(f_p,s)] = 'N'
# N = fp_s = simplify(diff(f_p,s))
# (simplify(cse(diff(T/Abs(T),s))))

print('\\begin{center}')
print('\\begin{align*}')

eq = {A1, A2, A3, A4, A5, A6}
theta = (dg_p, dg_d, s, b, d, Y)
for j, a in enumerate(eq):
    for i, var in enumerate(theta):
        print('grad[{},{}]'.format(j, i), '&=', cse(a.diff(var).subs(substitution_list)), '\\\\')

print('\end{align*}')
print('\\begin{center}')

simplify(Derivative(a, dg_p).doit().subs(substitution_list))

