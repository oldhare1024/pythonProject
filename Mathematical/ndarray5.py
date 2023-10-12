import numpy as np

a=np.arange(5)
b=np.arange(4.5,dtype=float)
c=np.arange(10,20,2)
d=np.linspace(start=1,stop=10,num=10,endpoint=True,retstep=False,dtype=int)
e=np.linspace(1,1,10,dtype=int)
f=np.logspace(1.0,2.0,num=10)
g=np.logspace(0,9,10,base=2,dtype=int)

print(a,b,c,sep=',')
print(d,e,sep='\n')
print(f,g,sep='\n')