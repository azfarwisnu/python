
#nilai pada matrikx 1
nilai1= [
	[2,4],
	[5,-6],
]

#nilai pada matrix 2

nilai2 = [
	[9,-3],
	[3,6],
]

#melakukan looping pada x denganrange 0 sampai panjang nilai 1
for x in range(0,len(nilai1)):
	#melakukan nested loop y dengan range 0 dan nilai 1 denganstart0 setiap loop
	for y in range(0, len(nilai1[0])):
		#lalu mencetak loop nilai x dan y serta nilai 2 x dan y
		#lalu di jumlahkan ketika di print, menggunakan end untuk sisinya berada diseblah
		print(nilai1[x][y] + nilai2[x][y], end=' ')
		#mencetak keseluruhan
	print("")
