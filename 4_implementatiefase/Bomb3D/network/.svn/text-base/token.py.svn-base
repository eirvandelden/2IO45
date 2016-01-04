#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import sys
import time
import uuid

from optparse import OptionParser
from Queue import Queue, Empty
from threading import Thread

class Server(object):
  WAIT = 120

  def __init__(self, name="<none>"):
    self.name = name
    self.identifier = uuid.uuid1().hex
  
    self.listen = self.Listen(self.identifier)
    self.listen.start()
        
    self.broadcast = self.Broadcast(self.identifier, name)
    self.broadcast.daemon = True
    self.broadcast.start()

  def stop(self):
    self.broadcast.stop = True
    self.listen.stop = True
    self.listen.sockets.remove(self.listen.server)
    for index, sock in enumerate(self.listen.sockets):
      print repr((index, sock))
      sock.send(" ".join([self.listen.sockets[(index + 1) % len(self.listen.sockets)].getpeername()[0], str(index)]))


  class Broadcast(Thread):
    INTERVAL = 0.1      # Interval between sending the messages

    def __init__(self, identifier, name):
      Thread.__init__(self)

      self.identifier = identifier
      self.name = name
      self.stop = False

    def run(self):
      self.broadcast = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
      self.broadcast.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

      sleep = time.sleep    # Hacks
    
      message = " ".join([self.identifier, self.name])
      while not self.stop:
        self.broadcast.sendto(message + "\r\n", ("<broadcast>", 11008))
        sleep(self.INTERVAL)


  class Listen(Thread):
    INTERVAL = 0.1

    def __init__(self, identifier):
      Thread.__init__(self)
        
      self.identifier = identifier
      self.stop = False

    def run(self):
      self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.server.bind(("", 11009))
      self.server.listen(5)

      self.sockets = [self.server]

      while not self.stop:
        reads = select.select(self.sockets, [], [], self.INTERVAL)[0]
        for read in reads:
          if read == self.server:
            client, address = self.server.accept()
            print 'client, ' + ':'.join(map(str, address))
            self.sockets.append(client)
          else:
            data = read.recv(4096)
            if data:
              pass
            else:
              self.sockets.remove(read)


class Token(object):
  def __init__(self, address, input, output):
    self.address = address
    self.identifier = uuid.uuid1().hex

    self.input = input
    self.output = output

    # if not self.address:
    #   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #   sock.bind(("", self.Broadcast.PORT))
                                    
    # while not self.stop and not self.address:
    #   try:
    #     data, address = sock.recvfrom(4096)
    #   except KeyboardInterrupt:
    #     self.stop = True
    #   else:
    #     identifier = data.rstrip()
    #     if not identifier == self.identifier:
    #       self.address = address[0]
    #       # print 'server, ' + ':'.join(map(str, address))
    #

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.address, 11009))

    data = self.socket.recv(4096)
    next, index = data.split(" ", 1)

    self.ring = self.Ring(next, input, output, int(index), self.identifier)
    self.ring.start()

  @staticmethod
  def search(timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 11008))

    found = {}

    tries = 20
    while tries > 0:
      reads = select.select([sock], [], [], 0.2)[0]
      for read in reads:
        data, address = read.recvfrom(4096)
        identifier, name = data.split(" ", 1)
        if identifier not in found:
          found[identifier] = {"name": name.rstrip(), "server": address[0]}

      tries = tries - 1

    return found

 
  class Ring(Thread):
    INTERVAL = 2

    def __init__(self, peer, input, output, index, identifier):
      Thread.__init__(self)

      self.identifier = identifier

      self.prev = self.next = None
      self.peer = peer
      self.index = index
      self.token = bool(index == 0)

      self.stop = False

      self.input = input
      self.output = output

      self.buffer = ''

    def run(self):
      self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.server.bind(("", 11010))
      self.server.listen(5)

      # self.sockets = [sys.stdin, self.server]
      self.sockets = [self.server]

      while not self.stop:
        reads = select.select(self.sockets, [], [], self.INTERVAL)[0]
        for read in reads:
          if read == self.server:
            if self.prev == None:
              self.prev, address = self.server.accept()
              # print 'connect, ' + ':'.join(map(str, address))
              self.sockets.append(self.prev)
          else:
            data = read.recv(4096)
            if data:
              if read == self.prev:
                lines = (self.buffer + data).split("\r\n")
                self.buffer = lines.pop()

                for line in lines:
                  if not line.strip():
                    continue;
                  identifier, command, arguments = line.split(" ", 2)

                  if not identifier == self.identifier and not command == "token":
                     self.next.send(line + "\r\n")
                     self.output.put(line)
                     # print "-- i", line
                  elif command == "token":
                    self.output.put("00000000000000000000000000000000 token ") # Padding spaties als argument
                    while True:
                      try:
                        message = self.input.get(False)
                        self._send(message)
                        self.output.put(" ".join([self.identifier, message]))
                        # print "-- o", message.strip()
                      except Empty:
                        break
                    #time.sleep(0.05)
                    self._send("token")
                    # print "-- t"
            else:
              sys.exit()
        
        if self.next == None:
          self.next = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          self.next.connect((self.peer, 11010))
          # self.next.send(" ".join([self.identifier, "HAI\r\n"]))
          if self.token:
            self._send("token")
          self.sockets.append(self.next)

    def _send(self, command, arguments=""):
      self.next.send(" ".join([self.identifier, command, arguments]) + "\r\n")

if __name__ == '__main__':
  parser = OptionParser()
  parser.add_option("-a", "--address",
                    action="store", dest="address", default=None)
  parser.add_option("-n", "--name",
                    action="store", dest="name", default="<None>")
  parser.add_option("-s", "--server",
                    action="store_true", dest="server", default=False)
  (options, args) = parser.parse_args()
 
  input = Queue()
  output = Queue()

  if options.server:
    print "A"
    server = Server(options.name)
    print "B"
    try:
      time.sleep(120)
    except KeyboardInterrupt:
      pass
    print "C"
    server.stop()
    print "D"
  else:
    servers = Token.search()
    print repr(servers)
    
    if len(servers):
      token = Token(servers[servers.keys()[0]]['server'], input, output)
