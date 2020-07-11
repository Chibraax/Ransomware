import socket 
import datetime
import threading





class Serveur() : 

    def __init__(self) : 
        'Init method'

    def run(self) : 

        sock.bind((host,port))
        print('[-] Server listenning on {}'.format(port))

        sock.listen()
        
        while True : 
            
            global conn
            global addr
            global it
            conn, addr = sock.accept()
            print('Connexion from {}'.format(addr))


 
            self.th3 = threading.Thread(target=self.next,daemon=True)
            self.th3.start()


    def next(self) : 

        data = conn.recv(2048)
        print(data.decode('Utf8'))
        print()

        tday = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        with open('c:\\Users\\Alex\\Desktop\\key.txt','a') as f : 

            f.write('Connexion from : {} , at : {} , Key : {}'.format(addr[0],tday,data.decode('Utf8')))
            f.write('\n')
    










host = '192.168.1.31'
port = 9984
memo = {}
sock = socket.socket()

serv = Serveur()
serv.run()


