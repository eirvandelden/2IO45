#!/usr/bin/env python

""" General networking class """

import Queue
import socket
import sys
import time
import uuid

from threading import Thread

__author__  = "Jeroen Habraken"
__version__ = "0.1"

class Discover(object):
  """ Peer discovery by broadcasting UDP packets """

  INTERVAL = 0.1

  def __init__(self, port=50414):
    queue = Queue.Queue()

    receive = self.Receive(port, queue)
    receive.start()

    send = self.Send(port, queue)
    send.daemon = True
    send.start()

    send.queue.put("HELO\r\n")

    wait = 0
    try:
      while wait < 1200 and receive.stop == False:
        wait = wait + 1
        time.sleep(self.INTERVAL)
    except KeyboardInterrupt:
      pass

    receive.stop = True
    
    send.queue.put("STOP\r\n")
    send.stop = True

    print receive.peers


  class Send(Thread):
    def __init__(self, port, queue):
      Thread.__init__(self)

      self.port = port
      self.queue = queue
      self.stop = False

    def run(self, retries=3):
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
      sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

      while not self.stop:
        try:
          ident = uuid.uuid1().hex
          message = ' '.join((ident, self.queue.get(True, Discover.INTERVAL)))
        except Queue.Empty:
          pass
        else:
          for retry in xrange(retries):
            sock.sendto(message, ("<broadcast>", self.port))

      sys.exit()


  class Receive(Thread):
    def __init__(self, port, queue):
      Thread.__init__(self)

      self.peers = set([])
      self.port = port
      self.queue = queue
      self.stop = False

      self._ident = []

    def run(self):
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.settimeout(Discover.INTERVAL)
      sock.bind(("", self.port))
      
      while not self.stop:
        try:
          message, address = sock.recvfrom(4096)
        except socket.timeout:
          pass
        else:
          ident, message = message.rstrip("\r\n").split(' ', 1)
          if ident not in self._ident:
            self._ident = (self._ident + [ident])[-3:]
  
            arguments = message.split(' ')
            handler = '_handle_' + arguments.pop(0).upper()
            if hasattr(self, handler) and callable(getattr(self, handler)):
              getattr(self, handler)(address[0], *arguments)

      sys.exit()

    def _handle_HELO(self, address):
      self.peers.add(address)
      self.queue.put("OLEH " + ' '.join(self.peers) + "\r\n")

    def _handle_OLEH(self, address, *peers):
      self.peers.add(address)
      for peer in peers:
        self.peers.add(peer)

    def _handle_STOP(self, address):
      self.stop = True

if __name__ == '__main__':
  Discover()
