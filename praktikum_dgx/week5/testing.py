import random
import math

def kombinasi(a,b):
    pilihan = ['gunting','batu','kertas']
    fix = ['gunting','batu','kertas']



    for x in range(0, a - 1):
        tampung = []
        for j in range(0, len(pilihan)):
            z = pilihan[j]
            for k in range(0,3):
                y = z + fix[k]
                tampung.append(y)
        pilihan = tampung


    for kuncian in b:
        for in in range(0, len(pilihan)):
            b[kuncian][pilihan[i]] = 0.1

    return b

def UserInput():
    print("Selamat Datang Di Gunting, Kertas, Batu")
    print("SILAHKAN PILIH!!!")
    print('GUNTING')
    print('KERTAS')
    print('BATU')

    a = 2
    status = True

    userjawab = []
    while status == True:
        print("Masukan pilihan : ", end = " ")
        r = int(input()).lower()
        userjawab.append(r)

        follow_unser_answer = userjawab[0:len(userjawab)]
        b = dict()
        b[0] = dict()
        b[1] = dict()
        b[2] = dict()

        if a >= len(follow_unser_answer):
            outputacak = random.randint(0,2)
            jawab = ''
            jawabanmu = ''
            if outputacak == 0:
                jawab = 'Batu'
            elif outputacak == 1:
                jawab = 'Gunting'
            elif outputacak == 2:
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
