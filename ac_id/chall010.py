'''
def get_score():
    score_list = []
    a = ''
    nilai = int(input('Masukkan skor (masukkan angka negatif untuk menyudahi): '))

    while nilai >= 0:
        score_list.append(nilai)
        nilai = int(input('Masukkan skor (masukkan angka negatif untuk menyudahi): '))

    print(score_list)
    return a



def jumlah_list(input_list):
    hasil_ganjil = 0
    hasil_genap = 0
    #nilai = 
    a = len(input_list)
    ganjil = input_list[0:a:2]
    genap = input_list[1:a:2]
    
    print(a)
   

    for x in(ganjil):
        hasil_ganjil += x

    for z in(genap):
        hasil_genap += z

        //wisnuazfar

    print('Total elemen indeks ganjil: ', hasil_genap)
    print('Total elemen indeks genap: ', hasil_ganjil)


x = [10,20,30,40,50]
jumlah_list(x)

mystr = 'yes'
mystr += 'no'
mystr += 'yes'
print(mystr)

mystring = 'abcdefg'
print(mystring[2:5])


def balik_string(input_string):
    kalimat = input_string
    panjang = len(kalimat) + 1
    for x in range(1,panjang):
        print(kalimat[-x],end="")


x = "aku"
balik_string(x)



def validasi_password(passwd):
    spesial_karakter = ['$', '@', '#', '%']
    panjang_benar = False
    ada_digit = False
    ada_huruf_besar = False
    ada_huruf_kecil = False
    ada_spesial_karakter = False
    
    if len(passwd) > 6:
        panjang_benar = True

        for ch in passwd:
            if ch.isdigit():
                ada_digit =  True
            if ch.isupper():
                ada_huruf_besar = True
            if ch.islower():
                ada_huruf_kecil = True

            if ch in spesial_karakter:
                ada_spesial_karakter =  True
            else:
                ada_spesial_karakter = False
            
        
        print(panjang_benar)
        print(ada_digit)
        print(ada_huruf_besar)
        print(ada_huruf_kecil)
        print(ada_spesial_karakter)


    if panjang_benar and ada_digit and ada_huruf_besar and ada_huruf_kecil and ada_pesial_karakter:
        output = True
    else:
        output = False

    return output

    


password = 'Password1234'
validasi_password(password)

'''

def main():
    tanggalstr = input('Masukkan tanggal dalam format hh/bb/tttt: ')
    #split masing-masing komponen
    haristr,bulanstr,tahunstr = tanggalstr.split('/')
    #Konversi bulanstr ke nama bulan
    bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    nilai = int(bulanstr)

    if  nilai > 12:
        print('Anda tidak memasukkan tanggal yang benar.')
    else:
        haristr = int(haristr)
        bulanstr = bulan[int(bulanstr)-1]
        print(haristr,bulanstr,tahunstr)

    

main()