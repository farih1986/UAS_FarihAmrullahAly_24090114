class Buah:
    def __init__(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self,nama): self.nama = nama
    def setWarna(self,warna): self.warna = warna
    def setRasa(self,rasa): self.rasa = rasa

# Contoh penggunaan
buah = Buah("Apel", "Merah", "Manis")
buah.setNama("Jeruk")

print(Buah.setNama())
print(Buah.setWarna())
print(Buah.setRasa())