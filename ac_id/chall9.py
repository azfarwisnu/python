'''
a = ['joko','anwar','budi','agus','ucup']
b=  0

print(a[:5])


z = [1,3,4,5]
x = z.index(3)
print(x)

angka = [1, 2, 3, 4, 5, 6, 7, 8]
print(angka[2])
print(angka[1:3])
print(angka[5:])
print(angka[-4:])
print(angka[::2])


x = [1, 2, 3, 4, 5]
x[0] = 99
print(x)


x = 4499

def hasil(nilai):
	a = [4353, 2314, 2956, 3382, 9362, 3900]
	a.insert(5,x)
	return a


z = hasil(x)
print(z)

buah = ['apel', 'anggur', 'mangga', 'jeruk'] 
print(buah[2])


nilai = [2] * 5 
print(nilai)


def ids(x):
	a = [4353, 2314, 2956, 3382, 9362, 3900]
	print(a)

ids(3)

list = [4353, 2314, 2956, 3382, 9362, 3900]
list.pop(5)
print(list)


my_tuple = ('apel', 'mangga', 'jambu')
my_list = list(my_tuple)
print(my_list)
'''

def main():
    nama_mhs = ('Budi', 'Dodi', 'Cindi', 'Kiki', 'Beti')
    for x in range(len(nama_mhs)):
    	print(nama_mhs[x])


main()