#1

from datetime import*
def diffDate(x):
    x = x.split('-')
    tanggal = date(int(x[0]), int(x[1]), int(x[2]))
    sekarang = datetime.date(datetime.now())
    hasil = tanggal - sekarang
    hasil = hasil.days
    print('Tanggal sekarang       : ', sekarang)
    print('Tanggal yang dipanggil : ', tanggal)
    print('Selisih tanggal        : ', hasil, 'hari')
    return hasil

diffDate('2021-1-27')
