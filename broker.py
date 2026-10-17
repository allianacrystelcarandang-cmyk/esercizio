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
           msg = messaggio.split(" ")
           topic=msg[1]
           if (topic=="sub"):
               print("SUBSCRIBER --")
               if topic in self.diz.keys():
                   self.diz[topic].append(self.addr)
                   print("client aggiunto al topic")
           else:
               mess=msg[2].encode("utf-8")
               print("publisher")
               if topic in self.diz :
                   for sock in self.diz[topic]:
                       sock.sendall(mess)
           print(self.diz)



if __name__ == '__main__':
       Main()
