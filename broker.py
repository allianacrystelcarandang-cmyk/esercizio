class BrokerMulti(threading.Thread):
   def __init__(self, client,addr,diz):
       super().__init__()
       self.sock=client
       self.addr=addr
       self.diz=diz

if __name__ == '__main__':
       Main()
