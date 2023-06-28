import queue

class myQueue:
    def __init__(self):
        self.items= queue.Queue()

    def isEmpty(self):
        return self.items.empty()
    
    def qAdd(self,item):
        self.items.put(item)

    def qOut(self):
        if not self.items.empty():
            return self.items.empty()
        else:
            return 'Data Antrian Kosong'
        
    def size(self):
        return self.items.qsize()
    
    def menu(self):
        pilih= 'y'
        while (pilih == 'y'):
            print('=========================')
            print('        Toko Kita        ')
            print('1. Masuk Antrian')
            print('2. Keluar Antrian')
            print('3. Cek Antrian')
            print('4. Banyak Antrian')
            print('5. Keluar')
            print('=========================')
            pilihan= str(input('Silahkan Masukkan Pilihan Anda: '))
            if (pilihan == '1'):
                object= str(input('Masukkan Nama: '))
                self.qAdd(object)
                print('Nama Anda '+object+' Telah Masuk Antrian')
                x= input('')
            elif (pilihan == '2'):
                temp= str(self.qOut())
                if temp != 'Data Antrian Kosong':
                    print('Nama '+ temp +' Telah Dilayani')
                else:
                    print('Antrian Kosong')
                x= input('')
            elif (pilihan == '3'):
                print(self.isEmpty())
                x= input('')
            elif (pilihan == '4'):
                print('Panjang Antrian yaitu: '+str(self.size()))
                x= input('')
            elif (pilihan == '5'):
                print('\nTerima Kasih Sudah Mampir di Toko Kami')
                print('Jangan Lupa Mampir Lagi ke Toko Kami ya')
                print(quit())
            else:
                pilih= 'n'

q= myQueue()
q.menu()
