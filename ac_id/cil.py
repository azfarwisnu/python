'''
angka = 1234567.456
print('{:20,.2f}'.format(angka,0))


a = int(input())


if a < 10:
	b = int(0)
else:
	b = int(99)


for x in range(1,11):
	x = x * x
	print(x)

string = ''
bar = int(input('Masukkan angka :'))
while bar >= 0:
	kol = bar

	while kol > 0:
		string = string + ' * '
		kol = kol - 1

	string = string + '\n'
	bar = bar - 1

print(string)


string = ""

x = int(input("Masukkan angka :"))
bar = x
# Looping Baris
while bar >= 0:
	# Looping Kolom Spasi Kosong
	kol = bar
	while kol > 0:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri < (x - (bar-1)):
		string = string + " * "
		kiri = kiri + 1		
	# Looping Kolom Bintang Sisi Kanan
	kanan = 1
	while kanan < kiri -1:
		string = string + " * "
		kanan = kanan + 1	

	string = string + "\n\n"
	bar = bar - 1
	
print (string)

def main():
# Variabel akumulator dan penghitung banyak input
    total = 0
    counter = 0
# Ambil angka pertama (tidak dikonversi ke int)
    num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): '))
# Jika karakter yang dimasukkan karakter kosong '',
# hentikan loop, jika bukan lanjutkan meminta angka
    while (num <= 0):
# Inkrementasi penghitung input
        counter += 1
# Akumulasikan total
        total += int(num)
# Ambil angka selanjutnya (tidak dikonversi ke int)
        num = input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): ')
# Tampilkan total jumlah dan rata-rata
    print('Rata-rata dari angka yang dimasukkan:', int(total/counter))
    return 

main()



def main():
	total = 0
	counter = 0

	num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif):'))

	while num != '':
		counter +=1
		total += int(num)
		num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif):'))
		print('Rata-rata dari angka yang dimasukkan:', total/counter)


main()
'''
def main():
# Variabel akumulator dan penghitung banyak input
    total = 0
    counter = 0
# Ambil angka pertama (tidak dikonversi ke int)
    num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): '))
# Jika karakter yang dimasukkan karakter kosong '',
# hentikan loop, jika bukan lanjutkan meminta angka
    while  num != '':
    
    	counter += 1
    	total += int(num)
    	num = int(input('Masukkan angka positif (akhiri dengan memasukkan angka negatif): '))
    	print('Rata-rata angka yang dimasukkan:', total/counter)
    	

main()