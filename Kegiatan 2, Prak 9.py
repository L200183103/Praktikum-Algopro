document = open("L200183103", "w")
document.write("L200183103 \n")
document.write("02/07/2000 \n")
document.write("Luckyta Afia Susanto \n")
document.write("Surakarta")
document.close()

import shelve
data = open("L200183103", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close

data = shelve.open("Luckyta")
data["newdata"] = [Nama, Kota, TL, NIM]
data.close()

data = shelve.open("Luckyta")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
