data_mahasiswa = []

def inputan():
    nim = int(input('Masukan NIM    : '))
    data_mahasiswa.append(nim)
    nama = input('Masukan Nama  : ')
    data_mahasiswa.append(nama)
    
inputan()
tambah = input('ingin tambah lagi?(y/t) : ')
if tambah == 'y':
    inputan()
else:
    print(data_mahasiswa)