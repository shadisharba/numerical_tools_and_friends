# https://github.com/google/jax

from jax import grad
import jax.numpy as jnp
from jax import jit, jacfwd, jacrev, hessian, jacobian
from jax import random as jrandom

def hessian2(fun):
    return jit(jacfwd(jacrev(fun)))
    
# Define some functions to take their derivates
def tanh(x):
    y = jnp.exp(-2.0 * x)
    return (1.0 - y) / (1.0 + y)

def abs_val(x):
    if x > 0:
        return x
    else:
        return -x

def sigmoid(x):
    return 0.5 * (jnp.tanh(x / 2) + 1)

def foo(v):
  return 0.5 * v.T @ v
  
# Evaluate the gradient of a scalar valued functions
grad_tanh = grad(tanh)
print(grad_tanh(1.0))
print(grad(grad(grad(tanh)))(1.0))

abs_val_grad = grad(abs_val)
print(abs_val_grad(1.0))
print(abs_val_grad(-1.0))

# Initialize random model coefficients
key = jrandom.PRNGKey(0)
key, W_key, b_key = jrandom.split(key, 3)
W = jrandom.normal(W_key, (3,))
b = jrandom.normal(b_key, ())

# Evaluate the jacobian and hessian of a scalar valued function
print('foo', foo(W))
print('jacobian', jacobian(foo)(W))
print('jacfwd', jacfwd(foo)(W))
print('grad', grad(foo)(W))
print('jacrev', jacrev(foo)(W))
print('hessian', hessian(foo)(W))
print('hessian2', hessian2(foo)(W))

# Evaluate gradients of a loss functions
def loss(W, b):
    inputs = jnp.array([[0.52, 1.12,  0.77],
                       [0.88, -1.08, 0.15],
                       [0.52, 0.06, -1.30],
                       [0.74, -2.49, 1.39]])
    targets = jnp.array([True, True, False, True])
    preds = sigmoid(jnp.dot(inputs, W) + b)
    label_probs = preds * targets + (1 - preds) * (1 - targets)
    return -jnp.sum(jnp.log(label_probs))

# Differentiate `loss` with respect to the first positional argument:
W_grad = grad(loss, argnums=0)(W, b)
print('W_grad', W_grad)

# Since argnums=0 is the default, this does the same thing:
W_grad = grad(loss)(W, b)
print('W_grad', W_grad)

# But we can choose different values too, and drop the keyword:
b_grad = grad(loss, 1)(W, b)
print('b_grad', b_grad)

# Including tuple values
W_grad, b_grad = grad(loss, (0, 1))(W, b)
print('W_grad', W_grad)
print('b_grad', b_grad)


# [check](http://www.acme.byu.edu/wp-content/uploads/2016/12/Vol1B-SympyAutograd-2017.pdf)
# https://pythonhosted.org/algopy/
# https://github.com/pierreablin/autoptim
# https://rlhick.people.wm.edu/posts/mle-autograd.html