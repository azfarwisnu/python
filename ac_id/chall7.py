'''
def cube(num):
	return num * num * num



def main():
	result = cube(4)
	print("result: ",result)



main()	


def half(number):
	return number / 2

def main():
	nilai = half(12)
	print(float(nilai))

main()


#The correct answer is: random.randrange()
#ython menyertakan library function yang berisi kumpulan module-module. Module adalah kumpulan fungsi-fungsi dan variable-variable (konstan).
#Pilihan terbaik adalah: Library Function
#blackbox


import math

def luas_lingkaran(radius):
	return math.pi * radius * radius

def keliling_lingkaran(radius):
	return 2 * math.pi * radius

def main():
	radius = float(input('Masukkan radius lingkaran (cm): '))
	luas = luas_lingkaran(radius)
	keliling = keliling_lingkaran(radius)
	print(f'\nLuas lingkaran dengan radius {radius:.2f}: {luas:.2f} cm2')
	print(f'\nKeliling lingkaran dengan radius {radius:.2f}: {keliling:.2f} cm')

main()


a = input('masukan a : ')
print(a + 50)
'''

a = int(input(''))
b = float(a * 0.23)

print(f'nilai {b:.2f}')
