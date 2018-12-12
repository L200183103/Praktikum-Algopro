import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50003))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = { 'name' : 'Luckyta Afia Susanto',
          'NIM' : 'L200183103',
          'generation' : '2018'}
while data.lower() != 'exit' :
    komm, addr = s.accept()
    while data.lower() !='exit':
            data = komm.recv(1024)
            if data.lower() == 'exit' :
                komm.send('ready!')
                s.close()
                break
            print 'Question: ', data
            if kamus.has_key(data):
                komm.send(kamus[data])
            else:
                komm.send('Your question is irrelevant')
