'''
def sum(nilai1, nilai2):
	result = nilai1 + nilai2
	return result


def main():
	umur1 = int(input("Masukan Umur A: "))
	umur2 = int(input("Masukan Umur B: "))
	total = sum(umur1, umur2)
	print("total umur adalah %d berikut" % total)


main()

def main():
	print('hello word')

if __name__ =='__main__':
	main()
	print("coba")


def sum(num1, num2):
    result = num1 + num2
    return result
def main():
    umur1 = int(input('Masukkan umur Anda: '))
    umur2 = int(input('Masukkan umur teman baik Anda: '))
    # Jumlahkan keduanya dengan memanggil fungsi sum
    total = sum(umur1, umur2)
    print('Umur Anda dan teman Anda: ', total, 'tahun.')
# Panggil fungsi main

main()
'''
# sapa_tamu.py
# Program ini mendemonstrasikan fungsi yang menerima
# sebuah argumen

def sapa(nama):
	print("Selamat datang, %s." %nama)

def main():
    nama = input('Masukkan nama Anda: ')
    sapa(nama)


main()