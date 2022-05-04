
import numpy as np
R = [2.0, 2.5, 2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 4.0]
R = np.arange(1.,5.,0.1)
Ebyk = []

Eplus = lambda r : np.sqrt((r-3)**2+1/100)
for r in R:

    Ep = Eplus(r)
    Ebyk.append(Ep)

print(Ebyk)
Eminus = -1*np.copy(Ebyk)

import matplotlib.pyplot as plt
'''
plt.plot(R, Ebyk)
print(R, Eminus)
plt.plot(R, Eminus)
plt.show()
'''
ratio = lambda r, sign: np.abs(1/((r-3)-sign * ((r-3)**2 + 1/100)**0.5))
R = np.arange(0, 3.5, 0.1)
lstplus = []
lstminus = []
for r in R:
    lstplus.append(ratio(r,1))
    lstminus.append(ratio(r,-1))

plt.plot(R, lstplus, 'r')
plt.plot(R, lstminus)
plt.show()
