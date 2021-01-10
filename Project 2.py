#2

from datetime import*
def dataBuku(kode, nama, judul):
    data = 'Data Buku.txt'
    file = open('Data Buku.txt', 'a')
    tanggal = datetime.date(datetime.now())
    tanggalKembali = tanggal + timedelta(days = 7)
    listData = [kode, nama, judul, str(tanggal), str(tanggalKembali)]
    file.write('|'.join(listData) + '\n')
    file.close()

ulang = 'y'
while ulang == 'y':
    kode = input ('Masukkan Kode Member  : ')
    nama = input ('Masukkan Nama Member  : ')
    judul = input('Masukkan Judul Member : ')
    dataBuku(kode, nama, judul)
    data = 'Data Buku.txt'
    ulang = input('\nUlangi lagi (y/n)     : ')
    print()
    ulang = ulang.lower()
