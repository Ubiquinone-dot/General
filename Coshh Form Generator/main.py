R = [2.0, 2.5, 2.8, 2.9, 3.0, 3.1, 3.2, 3.5, 4.0]
Ebyk = []
import numpy as np

Eplus = lambda r : np.sqrt((r-3)**2+1/100)
for r in R:

    Ep = Eplus(r)
    Ebyk.append(Ep)

print(R)