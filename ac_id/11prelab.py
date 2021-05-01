'''
def main():
	jumlah_ujian = 3
	jumlah_ujian += 1
	nilai_ujian = []
	tampung_rata = []
	mahasiswa = int(input('Masukkan jumlah mahasiswa: '))
	print('==================================================')
	mahasiswa += 1
	nilai_total = 0
	hasil = 0
	for x in range(1,mahasiswa):
		print('Masukkan nilai ujian untuk mahasiswa',x)
		print('--------------------------------------------------')
		for j in range(1,jumlah_ujian):
			nilai = input('Masukkan nilai ujian ke-' + str(j) + ': ')
			nilai = float(nilai)
			nilai_ujian.append(nilai)
			nilai_total += nilai
		print('==================================================')

		if x >= x:
			rata = float(nilai_total / 3)
			to_round = "{:.2f}".format(round(rata,2))
			tampung_rata.append(to_round)

		nilai_total = 0

	for k in range(1,mahasiswa):
			z = int(k-1)
			print('Rata-rata ujian mahasiswa ' + str(k) + ': ' + str(tampung_rata[z]))

main()



def main():

    kalimat = input("Masukkan sebuah teks: ")
    kalimat = kalimat.lower()

    karakter_list = {}
    for x in kalimat:
        if x not in karakter_list:
            karakter_list[x] = 1
        else:
            karakter_list[x] += 1
    
    highest = ""
    highest_val = 0
    for currentChar in karakter_list:
        currentValue = karakter_list[currentChar]
        if currentValue > highest_val:
            highest_val = currentValue
            highest = currentChar
    print('Karakter terbanyak: ', highest)
  

main()
'''

def cari_ruby(input_list):
	cari = 'Ruby'
	a = ''
	count = 0

	for x in input_list:
		if x == cari:
			count += 1
	print(count)
	return a

nama = ['Alan','Budi','Jodi','Susi']
cari_ruby(nama)