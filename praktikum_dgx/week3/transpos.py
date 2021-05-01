'''
import time 
import numpy as np 
import cupy as cp


print("Dengan Menggunakan Numpy / CPU")
s = time.time()

a = np.random.randint(10, size=(5,5))

c = a.transpose()
e = time.time()

print("Ini matriks A \n",a,"\n")

print("Di transpose \n",c,"\n")

print("waktu cpu : ", e - s, "detik")

print("================================== \n" * 2)

print("Dengan Menggunakan Cupy / GPU")

s = time.time()

a = np.random.randint(10, size=(5,5))

c = a.transpose()
cp.cuda.Stream.null.synchronize()
e = time.time()
print("Ini matriks A \n",a,"\n")

print("Di transpose \n",c,"\n")



import time 
import numpy as np 
import cupy as cp


print("Dengan Menggunakan Numpy / CPU")
s = time.time()

a = np.random.randint(10, size=(5,5))

c = a.transpose()
e = time.time()

print("Ini matriks A \n",a,"\n")

print("Di transpose \n",c,"\n")

print("waktu cpu : ", e - s, "detik")

print("================================== \n" * 2)

print("Dengan Menggunakan Cupy / GPU")

s = time.time()

a = np.random.randint(10, size=(5,5))

c = a.transpose()
e = time.time()
print("Ini matriks A \n",a,"\n")

print("Di transpose \n",c,"\n")
print("waktu GPU : ", e - s, "detik")
'''
import time
import numpy as np
import cupy as cp

s = time.time()
# membuat matriks dengan baris 1000 dan kolom 1000 dengan numpy
A = np.random.randint(10, size=(1000,1000))
# mencari transpose matriks dengan numpy
C = A.transpose()
e = time.time()
# menampilkan waktu hasil perhitungan dengan numpy
print("Waktu CPU :", e - s, "detik")

s = time.time()
# membuat matriks dengan baris 1000 dan kolom 1000 dengan cupy
A = cp.random.randint(10, size=(1000,1000))
C = A.transpose()
# mencari transpose matriks dengan cupy
cp.cuda.Stream.null.synchronize()
e = time.time()
# menampilkan waktu hasil perhitungan dengan cupy
print("Waktu GPU :", e - s, "detik")