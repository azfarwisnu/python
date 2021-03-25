#memberi nilai pada matrix
matrix = [[1,1],
		  [2,1],
		  [3,-3]]

#menampung nilai matrix baru

transport = [[0,0,0],
			[0,0,0]]

#melakukan loop dengan panjang matrix

for x in range(len(matrix)):
	#melakukan nested loop dengan panjang matrix [0]
	for j in range(len(matrix[0])):
		#lalu melakukan penukarang kolam menjadi baris
		transport[j][x] = matrix[x][j]

#mecnetak nilai transport dengan loop
for z in transport:
	print(z)
