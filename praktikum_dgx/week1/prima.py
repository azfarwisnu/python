awal = 11
akhir = 25

setlist = []

for x in range(awal, akhir+1):
	if x > 1:
		for j in range(2, x):
			if(x % j ==0):
				break
		else:
			print(x)
