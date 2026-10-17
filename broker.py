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


if __name__ == '__main__':
       Main()
