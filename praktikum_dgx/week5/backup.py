import random # Sementara aja ini pake random, buat belajar dari kesalahan
import math # Buat ngitung

def kemungkinanKombinasi(a, b):
    pilihan = ['0', '1', '2']
    kamus = ['0', '1', '2']

    for i in range(0, a - 1):
        f = []
        for j in range(0, len(pilihan)):
            x = pilihan[j]
            for k in range(0,3):
                y = x + kamus[k]
                f.append(y)
        pilihan = f
        
    for key in b:
        for i in range(0, len(pilihan)):
            b[key][pilihan[i]] = 0.1
            
    return b

def masukkanUser():
    print("Selamat datang di mainan Batu, Gunting, Kertas!")
    print("Lawan kamu adalah aku! Komputer paling cepat di komplek ini.")
    print("\n")
    
    print("Gas slurr")
    print("Silakan pilih:")
    print("0. Batu")
    print("1. Gunting")
    print("2. Kertas")
    
    a = 2 # Jumlah dictnya

    status = True
    
    jawabanUser = []
    while status == True:
        r = int(input('Masukan pilihan'))
        
        jawabanUser.append(r)
        
        ikutinJawabanUser = jawabanUser[0:len(jawabanUser) - 1]
        b = dict() # Kamus / Dictionary berisi jawaban user dari inputan sebelumnya
        b[0] = dict()
        b[1] = dict()
        b[2] = dict()

        # Permainan pertama, kita random aja. Bisa bisa mempelajari jawaban user
        if a >= len(ikutinJawabanUser):
            bimsalabim = random.randint(0, 2)
            jawab = ''
            jawabU = ''
            if bimsalabim == 0:
                jawab = 'Batu'
            elif bimsalabim == 1:
                jawab = 'Gunting'
            elif bimsalabim == 2:
                jawab = 'Kertas'
            
            if r == 0:
                jawabU = 'Batu'
            elif r == 1:
                jawabU = 'Gunting'
            elif r == 2:
                jawabU = 'Kertas'
            print("")
            print("Kamu: " + str(jawabU))
            print("Komputer: " + str(jawab))
        elif a < len(ikutinJawabanUser):
            b = kemungkinanKombinasi(a, b)
            c = math.pow(3, a)
            normalizer = c * 0.1

            for i in range(0, len(ikutinJawabanUser)):
                if i + a < len(ikutinJawabanUser):
                    key1 = ikutinJawabanUser[i]
                    key2 = ''.join(str(x) for x in ikutinJawabanUser[i:i + a])

                    lastVal = b[key1][key2]
                    b[key1][key2] # Update jumlah tiap kali user input

            for key in b:
                for i in b[key]:
                    if b[key][i] != 0.1:
                        lastVal = b[key][i]
                        base = ikutinJawabanUser[0 + a].count(key)
                        b[key][i] = lastVal / (base + normalizer)

            aInputTerakhir = ''.join(str(x) for x in ikutinJawabanUser[len(ikutinJawabanUser) - a:])

            probabilitasResp = []

            for key in b:
                pKey = round(ikutinJawabanUser.count(key), 3) / len(ikutinJawabanUser)
                pKey = round(pKey, 3)

                pengkondisianKey = b[key][aInputTerakhir]
                val = pengkondisianKey * pKey
                probabilitasResp.append(val)

            normalSum = 0

            for i in range(0, len(probabilitasResp)):
                normalSum = normalSum + probabilitasResp[i]

            finalResp = []

            for i in range(0, len(probabilitasResp)):
                finalResp.append(probabilitasResp[i]/normalSum)

            utilResp = []
            for i in range(0, len(finalResp)):
                if i == 0:
                    utilResp.append(finalResp[1] - finalResp[2])
                elif i == 1:
                    utilResp.append(finalResp[2] - finalResp[0])
                elif i == 2:
                    utilResp.append(finalResp[0] - finalResp[1])

            print(finalResp)
            pilihanKomputer = utilResp.index(max(utilResp))
            print(utilResp)

            jawab = ''
            jawabU = ''
            if pilihanKomputer == 0:
                jawab = 'Batu'
            elif pilihanKomputer == 1:
                jawab = 'Gunting'
            elif pilihanKomputer == 2:
                jawab = 'Kertas'

            if r == 0:
                jawabU = 'Batu'
            elif r == 1:
                jawabU = 'Gunting'
            elif r == 2:
                jawabU = 'Kertas'

            print("")
            print("Kamu: " + str(jawabU))
            print("Komputer: " + str(jawab))

masukkanUser()
