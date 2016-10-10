import numpy as np 
import matplotlib.pyplot as pp

x = np.linspace(0,10,50)
sinx = np.sin(x)
cosx = np.cos(x)

pp.plot(x,sinx)
pp.plot(x,cosx)

print(" inner product ",np.dot(sinx,cosx))
print(" outer product ",np.outer(sinx,cosx))

print(" size ",np.shape(np.outer(sinx,cosx)))
print(" size ",np.shape(sinx))
print(" size ",np.shape(np.transpose(sinx)))
print(" 25th row, 25th column element in outer product ",np.outer(sinx,cosx)[25,25])