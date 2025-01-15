class Queue:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} berhasil ditambahkan ke dalam antrian.")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong. Tidak ada item untuk dihapus.")
            return None
        removed_item = self.items.pop(0)
        print(f"{removed_item} berhasil dihapus dari antrian.")
        return removed_item

while True:
    print("Menu:")
    print("1. Tambahkan ke antrian")
    print("2. Hapus dari antrian")
    print("3. Keluar")


    pilihan = int(input('Masukan pilihan : '))

    if pilihan == 1:
        item = input("Masukkan yang ingin ditambahkan: ")
        enqueue(item)
    elif pilihan == 2:
        dequeue()
    elif pilihan == 3:
        print("Keluar mingat")
        break
    else:
        print("Patuhi peraturan yang ada.")
