import sys

def quitfunc(gamestate, player):
  print 'quitted'
  sys.exit()

  
def init(events):
  events.eNeatQuit.register(quitfunc)