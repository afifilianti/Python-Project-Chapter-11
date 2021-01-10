#3

from datetime import*
def tgl(x):
        file = open('Data Buku.txt', 'r')
        isi = file.read()
        data = isi.replace('\n','|')
        data = data.split('|')
        extract = data.index(kode)
        x = x.split('-')
        x = date(int(x[0]),int(x[1]),int(x[2]))
        i = data[extract + 4].split('-')
        n = date(int(i[0]), int(i[1]), int(i[2]))
        hasil = x - n
        hasil = hasil.days
        return hasil

def carikode(kode):
    try:
        file = open('Data Buku.txt', 'r')
        isi = file.read()
        data = isi.replace('\n','|')
        data = data.split('|')
        extract = data.index(kode)
        if kode in data :
            print('Data Peminjam Buku')
            print('Kode Member                  :', data[extract])
            print('Nama Member                  :', data[extract + 1])
            print('Judul Buku                   :', data[extract + 2])
            print('Tanggal Mulai Peminjaman     :', data[extract + 3])
            print('Tanggal Maks Peminjaman      :', data[extract + 4])
            kembali = str(input('Masukan Tanggal Pengembalian : '))
            tanggal = tgl(kembali)
            if tanggal > 0 :
                print('Terlambat Pengembalian       :' ,tanggal,'hari')
                denda = int(tanggal)*2000
                print('Denda                        : Rp.',denda)
            else:
                print('Tepat Waktu')
    
    except ValueError:
       print('Data tidak ditemukan')

ulang = 'y'
while ulang == 'y':
    kode = input('Masukkan Kode Member         : ')
    data = carikode(kode)
    ulang = input('\nUlangi ? (y/n)               : ')
    ulang = ulang.lower()
