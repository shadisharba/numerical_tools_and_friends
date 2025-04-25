# [TensorFlow examples](https://www.tensorflow.org/guide/autodiff)
# https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/guide/autodiff.ipynb
# https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/guide/advanced_autodiff.ipynb#scrollTo=DsOMSD_1BGkD
# https://www.tensorflow.org/api_docs/python/tf/GradientTape#jacobian

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# scalar
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x**2

# dy = 2x * dx
dy_dx = tape.gradient(y, x)
dy_dx.numpy()
print(dy_dx)

# nonscalar: tensors
w = tf.Variable(tf.random.normal((3, 2)), name='w')
b = tf.Variable(tf.zeros(2, dtype=tf.float32), name='b')
x = [[1., 2., 3.]]

with tf.GradientTape(persistent=True) as tape:
    y = x @ w + b
    loss = tf.reduce_mean(y**2)
[dl_dw, dl_db] = tape.gradient(loss, [w, b])
print(loss)
print(dl_db.shape)
print(dl_dw.shape)
print([var.name for var in tape.watched_variables()])

print(dl_dw)
print(tape.jacobian(loss,w))

# Assuming that X and Y are Tensorflow tensors and that Y depends on X
# from tensorflow.python.ops.parallel_for.gradients import jacobian
x = tf.Variable([1.0, 2.0])
with tf.GradientTape() as g:
    g.watch(x)
    y = x * x
jacobian = g.jacobian(y, x)
# jacobian value is [[2., 0.], [0., 4.]]
print(jacobian)