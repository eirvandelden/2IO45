"""
CubeLand: A simple AI testbed.
See the readme file for instructions.
This version (2007.7.28) uses a new and somewhat squirrelly 3D graphics
system, using OpenGL. Because the OpenGL was thrown in as an afterthought,
this version of the code is messy.
"""

import os
import time
import string

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
pygame.init()
from pygame.locals import *
SCREEN_SIZE = (640,480)

__author__ = "Kris Schnee"
__version__ = "2007.7.28"
__license__ = "Public Domain"

INPUT_FILEPATH = "to_world.txt"
OUTPUT_FILEPATH = "from_world.txt"
LOG_FILEPATH = "log.txt"
BOARD_SIZE = 8

class Robot:
    """The player's physical presence in the world."""
    def __init__(self,**options):
        self.name = options.get("name","Robot")
        self.coords = options.get("coords",(0,0))
        self.facing = options.get("facing",0)
        ## An object that the player is holding.
        self.holding = options.get("holding")
        ## Setting these options to True emulates a SHRDLU "skill crane."
        self.teleporting = options.get("teleporting",True)
        self.ghostly = options.get("ghostly",True)
        self.invincible = options.get("invincible",True)
    def Describe(self):
        text = "Player description: "+self.name
        text += "\nCoords: "+str(self.coords)+", facing "+str(self.facing)
        text += "\nHolding: "+str(self.holding)
        flags = []
        if self.teleporting:
            flags.append("Teleporting")
        if self.ghostly:
            flags.append("Ghostly")
        if self.invincible:
            flags.append("Invincible")
        if flags:
            text += "\nFlags: "+string.join(flags,", ")
        return text

class BlocksWorld:
    """A very simple virtual world, inspired by the classic SHRDLU."""
    def __init__(self,**options):
        global screen
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.done = False
        self.board_dirty = True
        self.turn = 0

        ## Auto-load all images in the graphics directory.
        self.textures = {}
        images = os.listdir(os.path.join("graphics","textures"))
        for image in images:
            try:
                self.LoadTexture(image,image[:-4])
            except:
                print "The filename '"+image+"' couldn't be loaded."

        pygame.font.init()
##        self.font = pygame.font.Font("ponderosa.ttf",14)
        self.message = "Ready for command."

        self.board = []
        for n in range(BOARD_SIZE*BOARD_SIZE):
            self.board.append([])

        self.shapes = {}
        self.colors = {}

        self.log = open(LOG_FILEPATH,"w")

        self.player = Robot(coords=(4,4))

        self.log.write("----- CubeLand Demo v"+__version__+" -----\nLog started "+time.strftime("%Y.%m.%d (%A) %H:%M")+".\nNow starting. Use Esc to quit, mouse to place crates\nand text files for AI input as per the instructions.\n\n")
        self.SetUpDemo()
        self.log.write(self.player.Describe()+"\n\n")

        self.test_valid = True ## Has nothing happened to disrupt the rules?

        self.camera_position = [40.0,-40.0,60.0]
        self.camera_target = [40.0,50.0,0.0]

        self.camera_angles = {}
        self.camera_angles["default"] = ([50.0,160.0,60.0],[50.0,-40.0,0.0])
        self.camera_angles["overhead"] = ([50.0,50.0,60.0],[50.0,50.0,0.0])

        self.cube_list = glGenLists(1)
        x, y, z = (5.0,5.0,5.0)
        glNewList(self.cube_list,GL_COMPILE)
        # Draw the cube.
        glBegin(GL_QUADS)
        # Top
        glTexCoord2f(0,0)
        glVertex3f(-x,-y,z)
        glTexCoord2f(1,0)
        glVertex3f(x,-y,z)
        glTexCoord2f(1,1)
        glVertex3f(x,y,z)
        glTexCoord2f(0,1)
        glVertex3f(-x,y,z)
        # Bottom
        glTexCoord2f(0,0)
        glVertex3f(-x,-y,-z)
        glTexCoord2f(1,0)
        glVertex3f(x,-y,-z)
        glTexCoord2f(1,1)
        glVertex3f(x,y,-z)
        glTexCoord2f(0,1)
        glVertex3f(-x,y,-z)
        # Front
        glTexCoord2f(0,0)
        glVertex3f(-x,y,-z)
        glTexCoord2f(1,0)
        glVertex3f(x,y,-z)
        glTexCoord2f(1,1)
        glVertex3f(x,y,z)
        glTexCoord2f(0,1)
        glVertex3f(-x,y,z)
        # Back
        glTexCoord2f(0,0)
        glVertex3f(-x,-y,-z)
        glTexCoord2f(1,0)
        glVertex3f(x,-y,-z)
        glTexCoord2f(1,1)
        glVertex3f(x,-y,z)
        glTexCoord2f(0,1)
        glVertex3f(-x,-y,z)
        # Left
        glTexCoord2f(1,1)
        glVertex3f(-x,-y,z)
        glTexCoord2f(0,1)
        glVertex3f(-x,y,z)
        glTexCoord2f(0,0)
        glVertex3f(-x,y,-z)
        glTexCoord2f(1,0)
        glVertex3f(-x,-y,-z)

        # Right
        glTexCoord2f(0,1)
        glVertex3f(x,-y,z)
        glTexCoord2f(1,1)
        glVertex3f(x,y,z)
        glTexCoord2f(1,0)
        glVertex3f(x,y,-z)
        glTexCoord2f(0,0)
        glVertex3f(x,-y,-z)

        glEnd()
        glEndList()


        # PYRAMID
        self.pyramid_list = glGenLists(1)
        x, y, z = (5.0,5.0,5.0)
        glNewList(self.pyramid_list,GL_COMPILE)
        # Draw the pyramid.
        glBegin(GL_QUADS)
        # Bottom
        glTexCoord2f(0,0)
        glVertex3f(-x,-y,-z)
        glTexCoord2f(1,0)
        glVertex3f(x,-y,-z)
        glTexCoord2f(1,1)
        glVertex3f(x,y,-z)
        glTexCoord2f(0,1)
        glVertex3f(-x,y,-z)
        glEnd()
        glBegin(GL_TRIANGLES)
        # Front
        glTexCoord2f(0,0)
        glVertex3f(-x,y,-z)
        glTexCoord2f(.5,1)
        glVertex3f(0,0,z)
        glTexCoord2f(1,0)
        glVertex3f(x,y,-z)
        # Back
        glTexCoord2f(0,0)
        glVertex3f(-x,-y,-z)
        glTexCoord2f(.5,1)
        glVertex3f(0,0,z)
        glTexCoord2f(1,0)
        glVertex3f(x,-y,-z)
        # Left
        glTexCoord2f(1,0)
        glVertex3f(-x,-y,-z)
        glTexCoord2f(.5,1)
        glVertex3f(0,0,z)
        glTexCoord2f(0,0)
        glVertex3f(-x,y,-z)
        # Right
        glTexCoord2f(0,0)
        glVertex3f(x,-y,-z)
        glTexCoord2f(.5,1)
        glVertex3f(0,0,z)
        glTexCoord2f(1,0)
        glVertex3f(x,y,-z)

        glEnd()
        glEndList()

    def Log(self,text):
        self.log.write("["+str(self.turn)+"] "+text+"\n")

    def LogInvalidityWarning(self):
        """Record the fact that something has changed the game's rules,
        which means that it some form of cheating may have happened."""
        self.log.write("*** Warning: Test may no longer be valid. ***")

    def SetUpDemo(self):
        self.LoadTest()
        
    def LoadTexture(self,filename,name):
        filename = os.path.join("graphics","textures",filename)
        texture = pygame.image.load(filename)
        self.textures[name] = len(self.textures) ## A texture number.
        texture_data = pygame.image.tostring(texture, "RGBX", 1 )
        glBindTexture(GL_TEXTURE_2D,len(self.textures)-1)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    def DrawScreen(self):
        if self.board_dirty:
            self.board_dirty = False

        #            ## Write out some information.
        #            self.screen.fill((0,0,0),(0,512,512,28))
        #            text_rendered = self.font.render(self.message,0,(255,255,255))
        #            self.screen.blit(text_rendered,(4,518))

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt( self.camera_position[0],self.camera_position[1],self.camera_position[2],
                       self.camera_target[0],self.camera_target[1],self.camera_target[2],
                       0,0,1 )

            glBindTexture(GL_TEXTURE_2D,self.textures["board"])
            glBegin(GL_QUADS)
            glTexCoord2f(0.0,0.0)
            glVertex3f(0.0,0.0,0.0)
            glTexCoord2f(1.0,0.0)
            glVertex3f(80.0,0.0,0.0)
            glTexCoord2f(1.0,1.0)
            glVertex3f(80.0,80.0,0.0)
            glTexCoord2f(0.0,1.0)
            glVertex3f(0.0,80.0,0.0)
            glEnd()

            # Draw the player.
            glLoadIdentity()
            gluLookAt( self.camera_position[0],self.camera_position[1],self.camera_position[2],
                       self.camera_target[0],self.camera_target[1],self.camera_target[2],
                       0,0,1 )
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA,GL_ONE)
            glDisable(GL_DEPTH_TEST)
            glColor4f(1.0,1.0,1.0,0.8)
            glBindTexture(GL_TEXTURE_2D,self.textures["board"])
            x,y = self.player.coords[0],self.player.coords[1]
            z = len(self.board[ y*BOARD_SIZE + x ])
            glTranslatef(10.0*x+5.0,10.0*y+5.0,10.0*z+5.0)
            glCallList(self.cube_list)
            glDisable(GL_BLEND)
            glEnable(GL_DEPTH_TEST)

            # Draw entites on the board.
            for y in range(BOARD_SIZE):
                for x in range(BOARD_SIZE):
                    contents = self.board[ y*BOARD_SIZE + x ]
                    if contents:
                        for z in range(len(contents)):
                            thing = contents[z]
                            texture = self.textures[thing]
                            glLoadIdentity()
                            gluLookAt( self.camera_position[0],self.camera_position[1],self.camera_position[2],
                       self.camera_target[0],self.camera_target[1],self.camera_target[2],
                       0,0,1 )
                            glBindTexture(GL_TEXTURE_2D,texture)
                            glTranslatef(10.0*x+5.0,10.0*y+5.0,10.0*z+5.0)
                            shape = self.shapes[thing]
                            if shape == "cube":
                                glCallList(self.cube_list)
                            elif shape == "pyramid":
                                glCallList(self.pyramid_list)



    def AddThing(self,thing,coords):
        self.board[ coords[1]*BOARD_SIZE + coords[0] ].append(thing)
        self.board_dirty = True

    def RemoveThing(self,coords):
        """Removes the "top" (last listed) object here and returns it."""
        tile = self.board[ coords[1]*BOARD_SIZE + coords[0] ]
        if tile:
            thing_removed = tile.pop()
            self.board_dirty = True
            return thing_removed
        else:
            return None ## There was nothing here to take.

    def HandleMouseClick(self,event):
        """Add/remove a crate where the player clicked."""
        tile = (event.pos[0]/64,event.pos[1]/64)
        if tile[0]<0 or tile[0]>=BOARD_SIZE or tile[1]<0 or tile[1]>=BOARD_SIZE:
            return ## Never mind; invalid tile location.
        if event.button == 1:
            self.AddThing("crate",tile)
        elif event.button == 3:
            self.RemoveThing(tile)

    def WaitForMessage(self):
        """If a file by the right name exists, respond."""
        if os.path.exists(INPUT_FILEPATH):
            ## Read a waiting message.
            f = open(INPUT_FILEPATH,"r")
            message = f.read()
            f.close()
            os.remove(INPUT_FILEPATH)

            ## Interpret the message and react.
            print "Got message: \""+message+"\""
            self.Log("Got message: \""+message+"\"")
            response = self.HandleMessage(message)

            ## Send and log the response.
            self.Log(response)
            f = open(OUTPUT_FILEPATH,"w")
            f.write(response)
            f.close()

            self.turn += 1

            ## Delay a bit to make sure the OS keeps up.
            time.sleep(2)

    def HandleMessage(self,message):
        response = "Not OK. Command not understood." ## Default reply.

        if not message:
            return response

        if message == "quit":
            response = "Quit OK."
            self.Log(response)
            self.done = True
            return response

        words = message.split()
        words[0] = words[0].lower()

        if words[0] == "configure":
            try:
                ## A fancy conversion that changes words[1:] to a dictionary.
                d = eval(string.join(w[1:],""))
                self.player.name = d.get("name",self.player.name)
                self.player.coords = d.get("name",self.player.coords)
                self.player.flags = d.get("name",self.player.flags)
                response = "Reconfigure OK. "+str(d)
                self.LogInvalidityWarning()
            except:
                response = "Reconfigure not OK."

        if words[0] == "move":
            try:
                coords = (int(words[1]),int(words[2]))
                print coords
                move_ok = self.MovePlayerTo(coords)
                if move_ok:
                    response = "Move OK."
                else:
                    response = "Move not OK."
            except:
                response = "Invalid command. Syntax: 'move # #'"

        elif words[0] == "grab":
            try:
                if self.player.holding:
                    response = "Grab not OK. Your hands are full."
                else:
                    thing_taken = self.RemoveThing(self.player.coords)
                    if thing_taken:
                        self.player.holding = thing_taken
                        shape = self.shapes[self.player.holding]
                        color = self.colors[self.player.holding]
                        response = "Grab OK. I got "+["a","an"][thing_taken[0] in "aeiou"]+" "+thing_taken+". Its shape is a "+shape+". Its color is "+str(color)+"."
                    else:
                        response = "Grab not OK. Nothing is here."
            except:
                response = "Invalid command. Syntax: 'grab'"

        elif words[0] == "drop":
            if not self.player.holding:
                response = "Drop not OK. My hands are empty."
            else:
                coords = self.player.coords
                stuff_here = self.board[ coords[1]*BOARD_SIZE + coords[0] ]
                if stuff_here and self.shapes[stuff_here[-1]] == "pyramid":
                    response = "Drop not OK. I can't put an object above a pyramid."
                else:
                    self.AddThing(self.player.holding,self.player.coords)
                    response = "Drop OK. I dropped "+self.player.holding+"."
                    self.player.holding = None

        elif words[0] == "look":
            try:
                if len(words) > 1:
                    if words[1] == "here":
                        response = ""
                        for y in range(8):
                            for x in range(8):
                                tile = self.board[y*8+x]
                                if tile:
                                    response += "@"
                                else:
                                    response += "."
                            response += "\n"
                        response = response[:-1]
                    elif words[1] == "down":
                        x, y = self.player.coords
                        tile = self.board[y*8+x]
                        num_items = len(tile)
                        if num_items == 0:
                            response = "There is nothing here."
                        elif num_items == 1:
                            response = "There is one item here: "+tile[0]+"."
                        else:
                            response = "There are "+str(num_items)+" objects here: "+string.join(tile,", ")+"."
                    elif words[1] == "hand":
                        if self.player.holding:
                            shape = self.shapes[self.player.holding]
                            color = self.colors[self.player.holding]
                            response = "I am holding "+self.player.holding+". Its shape is a "+shape+". Its color is "+str(color)+"."
                        else:
                            response = "I am holding nothing."
                    elif words[1] == "self":
                        response = str(self.player.coords)
                else:
                    response = str(self.board)
            except:
                response = "Invalid command. Syntax: 'look [here/hand/self/down/(nothing)]'"

        self.message = message+" --> "+response
        self.board_dirty = True
        return response

    def MovePlayerTo(self,coords):
        """Teleport to a certain position, if allowed."""
        if coords[0] < 0 or coords[0] >= BOARD_SIZE or coords[1] < 0 or coords[1] >= BOARD_SIZE:
            return False
        if self.player.teleporting:
            self.player.coords = coords
            return True
        else:
            self.Log("The player can't teleport.")
            return False

    def Go(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.done = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.done = True

                    ## Camera controls.
                    elif event.key == K_UP:
                        self.board_dirty = True
                        if self.camera_position[1] < 40.0:
                            self.camera_position[1] += 20.0
                            self.camera_position[2] += 10.0
                    elif event.key == K_DOWN:
                        self.board_dirty = True
                        if self.camera_position[1] >= -40:
                            self.camera_position[1] -= 20.0
                            self.camera_position[2] -= 10.0

                elif event.type == MOUSEBUTTONDOWN:
                    self.HandleMouseClick(event)

            self.WaitForMessage()

            self.DrawScreen()
            pygame.display.flip()
            self.clock.tick(3)

        if not self.test_valid:
            self.Log("\nNote: Test may not be valid. See warnings.")
        self.log.close()

    def LoadTest(self,filename="test.txt"):
        if not filename.endswith(".txt"):
            filename += ".txt"
        try:
            f = open(filename)
            text = f.read()
            f.close()
        except:
            print "Error: Couldn't find test file '"+filename+"'."
            return

        try:
            print "Loading test."
            import copy
            sections = text.split("\nKEY:\n")
            options = sections[0].split("\n")
            key, raw_layout = sections[1].split("\nLAYOUT:\n")
            self.test_name = options[0].replace("TEST NAME: ","")

            ## Special options.
            rules = options[1].replace("RULES: ","").replace(" ","").lower().split(",")
            rules_dict = {} ## Not really in use right now.
            if "teleporting" in rules:
                rules_dict["teleporting"] = True
                self.player.teleporting = True
            else:
                self.player.teleporting = False
            if "ghostly" in rules:
                rules_dict["ghostly"] = True
                self.player.ghostly = True
            else:
                self.player.ghostly = False
            if "invincible" in rules:
                rules_dict["invincible"] = True
                self.player.invincible = True
            else:
                self.player.invincible = False

            ## A key to the available objects.
            code = {}
            lines = key.split("\n")
            for l in lines:
                key, value = l.split("=")
                if value == "empty":
                    code[key] = []
                else:
                    color, shape, name = value.split(" ")
                    code[key] = [name]
                    self.shapes[name] = shape
                    self.colors[name] = color

            ## The board layout. For now it should just be eight rows of "."s and "c"s.
            raw_layout = raw_layout.replace("\n","")
            layout = []
            for c in raw_layout:
                layout.append(copy.copy(code.get(c,[])))

            self.board = layout
            self.board_dirty = True

            self.Log("Loaded test '"+self.test_name+"'\nBoard layout:\n"+raw_layout+"\n\n")

        except:
            print "Error: Couldn't load test file '"+filename+"'."
            return



def glInit():
    glClearColor(0.2,0.2,0.8,0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    angle = 60.0
    gluPerspective(angle, SCREEN_SIZE[0]/SCREEN_SIZE[1], 0.1, 250.0)
    glMatrixMode(GL_MODELVIEW)

def glEnable2d():
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0,640,0,480,-.1,.1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

def glDisable2d():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()


DISPLAY_FLAGS = OPENGL|DOUBLEBUF#|FULLSCREEN

os.environ["SDL_VIDEO_CENTERED"] = "1" # Center the graphics window.
screen = pygame.display.set_mode(SCREEN_SIZE,DISPLAY_FLAGS)
pygame.display.set_caption("CubeLand v"+__version__)

glInit()
glEnable(GL_TEXTURE_2D)

bw = BlocksWorld()
bw.Go()
