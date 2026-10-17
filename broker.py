import socket
import threading

class BrokerMulti(threading.Thread):
   def __init__(self, client,addr,diz):
       super().__init__()
       self.sock=client
       self.addr=addr
       self.diz=diz

   def readLine(self, sk):
       data = b''
       while (b'\n' not in data):
           data += sk.recv(1024)
           if not data: return b''
       return data.strip()

   def run(self):
           messaggio=self.readLine(self.sock).decode("utf-8")
           msg = messaggio.split(":")
           if msg[0] == "sub":
               topic=msg[1]
               print("SUBSCRIBER --")
               if topic in self.diz.keys():
                   self.diz[topic].append(self.sock)
                   print("client aggiunto al topic")
               else:
                   self.diz[topic]=[]
                   self.diz[topic].append(self.sock)
           else:
               topic=msg[1]
               mess=msg[2].encode("utf-8")
               print(mess)
               print("publisher")
               if topic in self.diz :
                   for sock in self.diz[topic]:
                       sock.sendall(mess)
           print(self.diz)

def Main():
   host = ''
   port = 1234
   diz = {}
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
   sock.bind((host, port))
   sock.listen(5)
   print("Broker listening...")

   while True:
       client, addr = sock.accept()
       print("Connected by", addr)
       thread = BrokerMulti(client, addr, diz)
       thread.daemon = True
       thread.start()
   sock.close()


if __name__ == '__main__':
       Main()
