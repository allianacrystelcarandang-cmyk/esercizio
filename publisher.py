import socket


def main():
   host= "127.0.0.1"
   port=1234
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))
   topic=input("Enter topic: ")
   message=input("Enter message: ")
   sock.sendall(f"pub:{topic}:{message}\n".encode())
   mess=readLine(sock).decode("utf-8")
   if mess=="si":
      print ("message sent --")
   elif mess=="no":
      print ("topic doesnt exist --")


def readLine(sk):
    data = b''
    while (b'\n' not in data):
        data += sk.recv(1024)
        if not data: return b''
    return data.strip()


if __name__ == "__main__":
   main()
import socket
