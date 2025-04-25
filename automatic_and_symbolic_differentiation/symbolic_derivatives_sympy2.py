from sympy import *

#init_printing(use_unicode = True)

dt = symbols('\Delta{t}')

# Previous time step values
n_a_l_old, n_a_p_old, n_ia_old = symbols('n^{(l)}_{a_{old}}, n^{(p)}_{a_{old}}, n_{ia_{old}}')

# Current active and inactive set
n_a_l, n_a_p, n_ia = symbols('n_a^{(l)}, n_a^{(p)}, n_{ia}')

# Segments (active and inactive)
N_a, N_ia, N_a_old, N_ia_old = symbols('N_{a}, N_{ia}, N_{a_{old}}, N_{ia_{old}}')

# Chain combination and scission probabilities
p_c, p_s = symbols('p_c, p_s')

# Compartment rates
alpha = 1 - (1 - p_c)**(N_ia + 1)
beta = 1 - (1 - p_s)**N_a
eta = 1 - (1 - p_c)**(N_a + 1)
nu = 1 - (1 - p_s)**N_ia

R1 = n_a_l - n_a_l_old + dt * beta * n_a_l + 2 * dt * eta * n_a_l
R2 = n_a_p - n_a_p_old - dt * alpha * n_ia - 4 * dt * eta * n_a_l
R3 = n_ia - n_ia_old - 2 * dt * alpha * n_a_l + 2 * dt * n_ia * (eta + nu)

# Terms involving the entire active set (1...p) are duplicated for the 'p'th term
# and also for the 'l'th term so this should evaluate to one and zero where
# appropriate
R4 = N_a - N_a_old - dt / (n_a_l + n_a_p) * (-beta * N_a * n_a_l + 2 * alpha * N_ia * n_ia - N_a *
                                             (alpha * n_ia - beta * n_a_l - beta * n_a_p + 2 * eta * (n_a_l + n_a_p)))
R5 = N_ia - N_ia_old - dt / n_ia * (beta * N_a * n_a_l - 2 * alpha * N_ia * n_ia - N_ia *
                                    (2 * beta * n_a_p + 2 * beta * n_a_l + 2 * beta * n_a_p + 2 * nu * n_ia))

# print(latex(R1), '\\\\')
# print(latex(R2), '\\\\')
# print(latex(R3), '\\\\')
# print(latex(R4), '\\\\')
# print(latex(R5))

# print('\n\nresidual vector\n', octave_code(R1, inline=False), '\n')
# print(octave_code(R2, inline=False), '\n')
# print(octave_code(R3, inline=False), '\n')
# print(octave_code(R4, inline=False), '\n')
# print(octave_code(R5, inline=False), '\n')

# NOTE: If we wanted to do CSE (common subexpression) that's done with this line of code
# print(latex(cse(simplify(Derivative(R1, n_a_l).doit()))), '\\\\')

# print('Derivatives R1')
# print(latex(simplify(Derivative(R1, n_a_l).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R1, n_a_p).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R1, n_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R1, N_a).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R1, N_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))))

print('Derivatives R2')
print(latex(simplify(Derivative(R2, n_a_l).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R2, n_a_p).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R2, n_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R2, N_a).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R2, N_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))))

print('Derivatives R3')
print(latex(simplify(Derivative(R3, n_a_l).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R3, n_a_p).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R3, n_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R3, N_a).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
print(latex(simplify(Derivative(R3, N_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))))

# print('Derivatives R4')
# print(latex(simplify(Derivative(R4, n_a_l).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R4, n_a_p).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R4, n_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R4, N_a).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R4, N_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))))
#
# print('Derivatives R5')
# print(latex(simplify(Derivative(R5, n_a_l).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R5, n_a_p).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R5, n_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R5, N_a).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))), '\\\\')
# print(latex(simplify(Derivative(R5, N_ia).doit().subs({alpha: 'alpha', beta: 'beta', eta: 'eta', nu: 'nu'}))))
