'''
tinggi = int(145)

if tinggi >= 145:
	print("Bisa menaiki wahana")
else :
	print("Tidak bisa menaiki wahana")

nilai = int(6)

if nilai % 2 == 0:
	print("Ini bilangan genap")
else:
    print("Ini bilangan ganjil")


def main():
	umur = int(input('Masukkan umur: '))
	bb = int(input('Masukkan berat badan (kg): '))
	tb = int(input('Masukkan tinggi badan (cm): '))
	imt = int(bb / ((tb/100) * (tb/100)))
	muda = int(45) >= umur
	kurus = int(22) >= imt

	if muda and kurus:	
		print('Tingkat resiko penyakit jantung Anda: RENDAH')
	elif muda or kurus:
		print('Tingkat resiko penyakit jantung Anda: SEDANG')
	else:
		print('Tingkat resiko penyakit jantung Anda: TINGGI')


main()

print(NOT False)

def main():
	ujian1 = float(input('Masukkan nilai ujian1: '))
	ujian2 = float(input('Masukkan nilai ujian2: '))
	lulus = ujian1 > 80 and ujian2 > 75

	if lulus:
		print('Anda lulus!')
	else:
		print('Anda tidak lulus!')



main()





def main():
	print('Angka\tKuadrat')
	print('---------------')

	for x in range(1,11):
		num = x ** 2
		print(f"{x}\t{num}")


main()


for i in range(0, 5):
	print(i)

for j in range(1, 10, 2):
print(j)


def main():
# Print baris judul
print('Angka\tKuadrat')
print('---------------')
# Print angka 1 s.d 10
# dan nilai kuadratnya
for num in range(1, 11):
kuadrat = num ** 2
print(f'{num}\t{kuadrat}')
main()



'''


'''

string = ''
bar = int(input('Masukkan angka :'))

#looping baris
while bar >= 0:
	kol = bar

	while kol > 0:
		string = string + ' * '
		kol = kol - 1

	string = string + '\n'
	bar = bar - 1

print(string)

print("    * ")
print("   * * ")
print("  * * *")
print(" * * * *")
print("* * * * *")
'''

def main():
	total_belanja = int(input('Total belanja : Rp '))
	bayar = total_belanja

	if total_belanja > 20000:
		print("Kamu mendapatkan bonus minuman dinginkan \ndan diskon 5%")
		diskon = total_belanja * (5/100)
		bayar = total_belanja - diskon
		print("Total yang harus dibayar: Rp", bayar)
		print("Terima kasih sudah berbelanja \nDatang lagi yaa...")


main()