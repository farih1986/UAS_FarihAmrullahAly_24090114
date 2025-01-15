class Buah:
    def init(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa
    
    def setNama(self, nama):
        self.nama = nama
    
    def setWarna(self, warna):
        self.warna = warna
    
    def setRasa(self, rasa):
        self.rasa = rasa
    
    def information(self):
        return f'Nama: {self.nama}, Warna: {self.warna}, Rasa: {self.rasa}'

buah1 = Buah ('Mangga', 'Jingga','Manis')

buah1.setNama('Mangga')
buah1.setWarna('Jingga')
buah1.setRasa('Manis')

print(buah1.information())
