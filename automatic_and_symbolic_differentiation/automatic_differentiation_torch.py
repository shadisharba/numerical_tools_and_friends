import torch
import time

class TicTocTimer:
    def __init__(self):
        self.running = False
        self.t = 0.0

    def tic(self):
        self.t = time.time()
        self.running = True

    def toc(self, str=None):
        T = time.time()
        assert (not self.running), 'error: timer not started; aborting'
        if (str is None):
            print('### elapsed time  %12.3f sec' % (T - self.t))
        else:
            print('### elapsed time  %12.3f sec  %s' % (T - self.t, str))

    def stop(self):
        self.running = False

N = 10
x = torch.rand(size=(N, 3))
x.requires_grad_(True)
# f = lambda x: (x**2).sum(1) + x.mean(1)
f = lambda x: (x**2).mean(1)  #+ x[:,1]*x[:,2]
F = f(x)
print('shape of function: ', F.shape)
y = torch.autograd.grad(F, x, torch.ones(N), retain_graph=True, create_graph=True, allow_unused=True)[0]
print('df_i / dx_j       ....  ', y)
for i in range(3):
    try:
        z = torch.autograd.grad(y[:, i], x, torch.ones(N), retain_graph=(i < 2), create_graph=(i < 2), allow_unused=True)[0]
    except:
        z = torch.zeros_like(x)
    print('d^2 f_%d / dx_j^2  ....  ' % (i), z)
