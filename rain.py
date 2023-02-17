import numpy as np
import random as r

rain = r.sample(range(1, 48), 47)
a = rain[0:7]
b = rain[7:15]
c = rain[15:22]
d = rain[22:29]
e = rain[29:36]
f = rain[36:43]
g = rain[43:50]
med = [1, 2, 3, 4, 5, 6, 7]
med[0] = np.median(a)
med[1] = np.median(b)
med[2] = np.median(c)
med[3] = np.median(d)
med[4] = np.median(e)
med[5] = np.median(f)
med[6] = np.median(g)
M = np.median(med)
print(int(M))
