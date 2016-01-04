#!/usr/bin/env python

import select
import socket
import time
import uuid

from threading import Thread

PORT = 50414
INTERVAL = 1

class Network(object):
  def __init__(self):
    # Generate a unique identifier for the node
    self.identifier = uuid.uuid1().hex
    self.stop = False

    # Start a listening socket, for peer connections
    tcp = self.TCP(self.identifier)
    tcp.start()

    time.sleep(1) # Wait for the TCP socket to properly bind itself, fuck OS X ;)
    print "self", tcp.server.getsockname()

    # Start broadcasting our presence
    broadcast = self.Broadcast(self.identifier, tcp.server.getsockname()[1])
    broadcast.daemon = True
    broadcast.start()

    # Start searching for other peers
    try:
      # Create a listening socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.bind(("", PORT))
    except socket.error:
      print "You might be fucked .."
      # tcp.stop = True
    else:
      self.connected = False
      while not tcp.parent and not self.stop:
        # Wait for other broadcast packets
        try:
          data, address = sock.recvfrom(4096)
        except KeyboardInterrupt:
          self.stop = tcp.stop = True
        else:
          # Check if it's not our own broadcast
          identifier, port = data.rstrip().split(" ")
          if not identifier == self.identifier:
            try:
              # Connect to the new peer via TCP
              parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              parent.connect((address[0], int(port)))
            except socket.error, e:
              pass
            else:
              tcp.parent = parent

  class Broadcast(Thread):
    def __init__(self, identifier, port):
      Thread.__init__(self)

      self.identifier = identifier
      self.port = port
      self.stop = False

    def run(self):
      # Create a sending socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
      # Send a message every second containing our identifier and port of the TCP socket
      message = " ".join([self.identifier, str(self.port)])      
      while not self.stop:
        sock.sendto(message + "\r\n", ("<broadcast>", PORT))
        time.sleep(1)

  class TCP(Thread):
    def __init__(self, identifier):
      Thread.__init__(self)

      self.identifier = identifier
      self.stop = False

    def run(self):
      # Create a listening socket
      self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.server.bind(('', 0))
      self.server.listen(5)

      self.parent = None

      # Keep a list of sockets for the select loop
      self.sockets = [self.server]
      
      while not self.stop:
        
        reads = select.select(self.sockets, [], [], INTERVAL)[0]
        for read in reads:
          if read == self.server:
            # A new TCP connection is made, accept this and add it to the sockets
            client, address = self.server.accept()
            self.sockets.append(client)
          else:
            data = read.recv(4096)
            # If data is received ..
            if data:
              # .. broadcast it to all the other sockets
              for sock in self.sockets:
                if sock == self.server or sock == read:
                  continue
                sock.send(data)
              print data
            # or when no data is received, the sockets was closed, remove it
            else:
              read.close()
              self.sockets.remove(read)

        # TODO check for loops
        if self.parent and self.parent not in self.sockets:
          print [sock.gethostname() for sock in self.sockets]
          print self.sockets
          print "remote", self.parent.getpeername()
          self.sockets.append(self.parent)
      
      self.server.close()

if __name__ == "__main__":
    # Main thread
    network = Network()
