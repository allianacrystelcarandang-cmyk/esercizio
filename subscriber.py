import socket


def main():
   host= "127.0.0.1"
   port=3087
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))
   topic=input("Enter topic: ")
   message=input("Enter message: ")
   sock.sendall(f"sub:{topic}\n".encode())
   while True:
       print(sock.recv(1024).decode())




if __name__ == "__main__":
   main()
