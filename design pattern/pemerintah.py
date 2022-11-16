class Pemerintah():
    # Informasi
    kebijakan = None
    pajak = 0

    # Instance
    __instance = None

    # Private Constructor
    def __init__(self):
        if Pemerintah.__instance != None:
            raise Exception("Pemerintah sudah terbentuk!")
        else:
            Pemerintah.__instance = self

    # Static Access Method
    @staticmethod
    def getInstance():
        if Pemerintah.__instance == None:
            Pemerintah()
        return Pemerintah.__instance

from pemerintah import Pemerintah

pemindo = Pemerintah.getInstance()

pemindo.kebijakan = "Kebebasan Berpendapat"
pemindo.pajak = 1000

print(pemindo.kebijakan)
print(pemindo.pajak)

from pemerintah import Pemerintah

# buat 2 objek instance
pemindo = Pemerintah.getInstance()
pemkot = Pemerintah.getInstance()

pemindo.kebijakan = "Indonesia Sebagai Negara Agraris"
pemindo.pajak = 1000

pemkot.kebijakan = "Didalam Kota Dilarang Pacaran"
pemkot.pajak = 9999

print(pemindo.kebijakan) 
print(pemindo.pajak) 

from pemerintah import Pemerintah

# buat 2 objek instance
pemindo = Pemerintah.getInstance()
pemkot = Pemerintah.getInstance()

if (pemindo == pemkot) :
    print("Mereka Objek yang sama")
else:
    print("Mereka Objek yang berbeda")


