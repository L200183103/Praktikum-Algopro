import socket

hostname = 'localhost'
pesan = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Automatic answering machine is ready"
while pesan.lower() != 'exit' :
    pesan = raw_input("Question: ")
    s.send(pesan)
    if pesan.lower() != 'exit':
        response = s.recv(1024)
        print 'The answer: ', response
response = s.recv(1024)
print 'The answer: ',response
s.close()
