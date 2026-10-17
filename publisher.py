import socket


def main():
   host= "127.0.0.1"
   port=1234
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))
   topic=input("Enter topic: ")
   message=input("Enter message: ")
   sock.sendall(f"pub:{topic}:{message}\n".encode())


if __name__ == "__main__":
   main()
import socket
