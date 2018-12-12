import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50004))
s.listen(5)
print "Menghitung Luas Bola"
data = ''
while data.lower() != ' quit' :
    komm, addr = s.accept()
    sisi = 0
    while data.lower() != 'quit':
        data = komm.recv(1024)
        if data.lower() == 'quit':
            s.close()
            break
        print'Command: ', data
        try:
                sisi = int(data)
                komm.send('data tersimpan')
        except ValueError:
                if data.lower() == 'hitung':
                        respon = 'luas bola dengan sisi '+str(sisi)+' = '
                        komm.send(respon)

                        
                else:
                        komm.send('unknown command')
                    
