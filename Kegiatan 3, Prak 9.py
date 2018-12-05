import shelve

data = open("L200183103", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close()

data = shelve.open("Luckyta")
data["newdata"] = [NIM, TL, Nama, Kota]
data.close()
