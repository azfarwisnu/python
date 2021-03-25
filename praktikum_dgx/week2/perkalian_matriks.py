#nilai 1 pada matriks
nilai1 = [
	[5, 0],
    [2, 6],
]

#nilai2 pada matriks
nilai2 = [
	[1, 0],
    [4, 2],
]


#matix3 yang menampung nilai perkalian
nilai3 = []

#melakukan loop x dengan range 0 sampai panjang nilai 1
for x in range(0, len(nilai1)):
	#membaut row untuk menampung nilai sementara
	row = []
	#melakukan loop y dengan rang 0 hingga nilai1 dengan radius 0
	for y in range(0, len(nilai1[0])):
		#deklarasi nilai hasil 0
		hasil = 0
		#melakukan loop z dengan range 0 hingga range nilai
		for z in range(0, len(nilai1)):
			#var hasil melakukan penjulahan yaitu nilai dan nilai1 loop x z dan nilai 2 loop x z
			hasil = hasil + (nilai1[x][z] * nilai2[z][y])
			#lalu di apped hasil ke arrow dimasukan
		row.append(hasil)
		#kemudian diappedn kembali hasil dari row ke nilai 3
	nilai3.append(row)

#lalu melakukan loop dari hasil tampung nilai 3 untuk menampilkan 
#hasil dari perkalian matriks
for x in range(0, len(nilai3)):
	#melakukan nested loop kembali dengan range 0 hingga panjang nilai3dari[0]
	for y in range(0, len(nilai3[0])):
		#cetak loop nilai3 dan x dan y lalu memberikan end kanan dan spasi
		print(nilai3[x][y], end=' ')
	print("")
