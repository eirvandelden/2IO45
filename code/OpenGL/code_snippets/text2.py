from gles import *
from fixedMath import *    # fixed point operations
from serial import *       # deserializer  
 
 
# GLFontChar structure as stored in file
class GLFontCharFile:
    dx = dy   = 0   # all floats
    tx1 = ty1 = 0 
    tx2 = ty2 = 0
 
 
# GLFontHeaderFile structure as stored in file
class GLFontHeaderFile:
    tex = 0                    # int32
    texWidth = texHeight = 0   # int32
    startChar = endChar = 0    # int32
    chars = 0                  # uint32
 
 
# Font class
class GLFont:
    
    ''' "private" members '''
    
    # a single character
    class GLFontChar:
        dx = dy   = 0    # all GLfixed
        tx1 = ty1 = 0
        tx2 = ty2 = 0
        
        
    # font archive header
    class GLFontHeader:
        tex = 0                    # GLuint
        texWidth  = texHeight = 0  # int
        startChar = endChar = 0    # int
        chars     = None           # memory buffer
        
        def __init__(self):
            chars = []
        
        
    # font header
    __header = None
    
    # vertices, texture coordinates and indices (gles.arrays)
    __vertices  = None
    __texCoords = None
    __indices   = None
    
    
    ''' private API '''
    def loadFile (self, filename):
        
        # Open input file
        des = Deserializer (filename)
        
        # Read file header
        self.__header.texWidth  = des.readLong()        
        self.__header.texWidth  = des.readLong()
        self.__header.texHeight = des.readLong()
        self.__header.startChar = des.readLong()
        self.__header.endChar   = des.readLong()
        self.__header.chars     = des.readUlong()
        
        # Allocate space for character array         
        numChars = self.__header.endChar - self.__header.startChar + 1        
        self.__header.chars = [GLFont.GLFontChar() for i in range(numChars)]
        
        # Read character array
        for i in range (numChars):
            self.__header.chars [i].dx  = float2fixed (des.readFloat () )            
            self.__header.chars [i].dy  = float2fixed (des.readFloat () )
            self.__header.chars [i].tx1 = float2fixed (des.readFloat () )
            self.__header.chars [i].ty1 = float2fixed (des.readFloat () )
            self.__header.chars [i].tx2 = float2fixed (des.readFloat () )
            self.__header.chars [i].ty2 = float2fixed (des.readFloat () )            
        
        
        # Read texture pixel data
        numTexBytes = self.__header.texWidth * self.__header.texHeight * 2        
        
        texBytes = des.readBytesAsString (numTexBytes)
        
        data = str(texBytes)
        
        
        # Create OpenGL texture        
        glBindTexture   (GL_TEXTURE_2D, self.__header.tex)
        glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexEnvf (GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
 
	glTexImage2D (GL_TEXTURE_2D, 0, GL_LUMINANCE_ALPHA, self.__header.texWidth, self.__header.texHeight, 0, GL_LUMINANCE_ALPHA, GL_UNSIGNED_BYTE, data)
	
                      
	# Free texture pixels memory
        del texBytes
 
	# Close input file
        des.close ()
        del des
               
 
    def __destroy (self):        
        # Delete the character array if necessary
        del self.__header.chars [:]
        self.__header.chars = []
        
 
    
    ''' "public" API '''
    
    def __init__(self,  filename):
        # Initialize header to safe state
        self.__header = GLFontHeaderFile()
        
        self.__header.tex = 0        
        self.__header.texWidth = 0
	self.__header.texHeight = 0
	self.__header.startChar = 0
	self.__header.endChar = 0
	self.__header.chars   = []        
 
	# OpenGL texture
        self.__header.tex = glGenTextures (1)
                       
        # Destroy the old font if there was one, just to be safe
        self.__destroy ()
        
        # load file
        self.loadFile (filename)
        
        # create gles.arrays to use in rendering
        
        v = [0] * 4*2     # 4 2D vertices
        t = [0] * 4*2     # 4 2D texture coordinates 
        i = [1, 2, 0, 3]  # a quad
         
        self.__vertices = array (GL_FIXED, 2, v)
        self.__texCoords = array (GL_FIXED, 2, v)
        self.__indices =  array (GL_UNSIGNED_BYTE, 1, i)
        
        v = None
        t = None
        i = None                 
        
    
    def free (self):
        # Destroy the font
        self.__destroy()
 
	# delete texture
        t = [self.__header.tex]
        glDeleteTextures (t)
        
        # free arrays
        del self.__vertices
        del self.__texCoords
        del self.__indices
    
    
    # Sets required states for the font.
    def beginDraw (self):
        glEnable (GL_BLEND)
        glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable (GL_TEXTURE_2D)
        glEnableClientState (GL_TEXTURE_COORD_ARRAY)
 
    #Turns off required states.
    def endDraw (self):
        glDisable (GL_BLEND)		
        glDisable (GL_TEXTURE_2D)
        glDisableClientState (GL_TEXTURE_COORD_ARRAY)
    
    
    # Retrieves the texture dimensions. Returns a tuple with the values
    def getTexSize (self):
        return (self.__header.texWidth, self.__header.texHeight)
    
    # Retrieves the character interval as a tuple.
    def getCharInterval (self):
        return (self.__header.startChar, self.__header.endChar)
    
    # Retrieves the dimensions of a character as a tuple.
    def getCharSize (self, character):
        
        # Make sure character is in range
        character = ord(character)
        if character < self.__header.startChar or character > self.__header.endChar:
            
            # Not a valid character, so it obviously has no size
            return (0,0)
        else:
            
            fontChar = self.__header.chars [character - self.header.startChar]
            
            # retrieve character size
            w = fixed2int (fixed_mul (fontChar.dx, int2fixed (self.__header.texWidth) ) )
            h = fixed2int (fixed_mul (fontChar.dy, int2fixed (self.__header.texHeight) ) )
            
            fontChar = None
            
            return (w,h)
    
    
    # Retrieves the dimensions of a string as a tuple.
    def getStringSize (self, text):
	
	# Height is the same for now...might change in future
	height = fixed2int (fixed_mul (self.__header.chars [self.__header.startChar].dy, int2fixed (self.__header.texHeight) ) )
	
	# texWidth as fixed
	texWidthx = int2fixed (self.__header.texWidth)
	
	# Calculate width of string	
	widthx = 0
	
        for c in text:            
            # Make sure character is in range
            c = ord(c)            
            if c < self.__header.startChar or c > self.__header.endChar:                
                continue
            
            # get glfont character object
            fontChar = self.__header.chars [c - self.__header.startChar]
            
            # get width and height
            widthx += fixed_mul (fontChar.dx, texWidthx)
            
            fontChar = None
            
        # return width
        return (fixed2int (widthx), height)
    
    
    # Renders a string. Reference point is top-left (all fixed point values).
    def drawString (self, text, x, y):
        
        # vertex arrays to render the string	
        glVertexPointer  (2, GL_FIXED, 0, self.__vertices)
        glTexCoordPointer (2, GL_FIXED, 0, self.__texCoords)
        
        # Bind texture        
        glBindTexture (GL_TEXTURE_2D, self.__header.tex)
 
	# Loop through characters
	for c in text:
 
            c = ord (c)
            
            # Make sure character is in range
            if c < self.__header.startChar or c > self.__header.endChar:
                continue
 
            # Get pointer to glFont character
            fontChar = self.__header.chars [c - self.__header.startChar]
 
            # Get width and height
            width  = fixed_mul (fontChar.dx, int2fixed (self.__header.texWidth) )
            height = fixed_mul (fontChar.dy, int2fixed (self.__header.texHeight) )
            
            # Specify texture coordinates
            self.__texCoords [0] = fontChar.tx1 ; self.__texCoords [1] = fontChar.ty1            
            self.__texCoords [2] = fontChar.tx1 ; self.__texCoords [3] = fontChar.ty2
            
            self.__texCoords [4] = fontChar.tx2 ; self.__texCoords [5] = fontChar.ty2
            self.__texCoords [6] = fontChar.tx2 ; self.__texCoords [7] = fontChar.ty1
 
            # and vertices
            self.__vertices [0] = x;          self.__vertices [1] = y
            self.__vertices [2] = x;          self.__vertices [3] = y - height
 
            self.__vertices [4] = x + width;  self.__vertices [5] = y - height
            self.__vertices [6] = x + width;  self.__vertices [7] = y
 
            # draw
            glDrawElements (GL_TRIANGLE_STRIP, 4, GL_UNSIGNED_BYTE, self.__indices)
 
            # Move to next character
            x += width