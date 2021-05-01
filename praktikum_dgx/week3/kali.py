import time 
import numpy as np 

s = time.time()

a = np.random.randint(10, size=(1000,1000))
b = np.random.randint(10, size=(1000,1000))

c = a.dot(b)
e = time.time()

print("Ini matriks A \n",a,"\n")
print("Ini matriks B \n",b,"\n")

print("waktu cpu : ", e - s, "detik")