#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def client_login():
  """Sets up handling for incoming clients."""
  while True:
    client, client_address = server.accept()
    print("%s:%s has connected." % client_address)
    addresses[client] = client_address
    Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
  """Handles a single client connection."""
  # Quando adicionar o cliente manda mensagem dizendo que entrou
  # msg = "%s has joined the chat!" % name
  # broadcast(bytes(msg, "utf8"))
  # Adiciona o username na lista
  clients[client] = "username"
  c = client

  while True:
    msg = client.recv(BUFSIZ).decode("utf8")
    if msg != "{quit}":
      print(msg)
      broadcast(msg, "username: ")
    else:
      # Removes the client
      client.close()
      del clients[client]
      # Bye message
      msg = "username has left the chat."
      broadcast(msg, "")
      break


def broadcast(msg, prefix=""):  # prefix is for name identification.
  """Broadcasts a message to all the clients."""
  if clients:
    for sock in clients:
      sock.send(msg)


clients = {}
addresses = {}

HOST = ''
PORT = 5000
BUFSIZ = 1024
ADDR = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)

if __name__ == "__main__":
  server.listen(5)
  print("Waiting for connection...")
  thread = Thread(target=client_login)
  thread.start()
  thread.join()
  server.close()
