import socket
import base64
import sys
import time


HOST = 'localhost'
PORT = 31000

with open(sys.argv[1], 'rb') as f:
    img = f.read()
    #print (base64.b64encode(img))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    #img = base64.b64encode(img).decode('utf-8')

    print ("send")
    s.sendall(base64.b64encode(img))
    print ("complete")
    s.shutdown(1)
    print ("complete2")

    #time.sleep(90)

    data = s.recv(300000)

    #print(data)

    receiveimg = base64.b64decode(data)
    
    f2 = open("receive.png", 'bw')
    f2.write(receiveimg)
    f2.close()
