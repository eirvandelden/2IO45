from __future__ import division
import math
import pygame

CAMERASPEED = 0.1
ROTATESPEED = 0.05

class tVector3():	# Extended 3D Vector Struct
    def __init__(self, new_x, new_y, new_z): # Init Constructor	 
        self.x, self.y, self.z = new_x, new_y, new_z
    # overload the + operator
    def __add__(self, vVector):
        return tVector3(vVector.x + x, vVector.y + y, vVector.z + z)
    # overload the - operator
    def __sub__(self, vVector):
        return tVector3(self.x - vVector.x, self.y - vVector.y, self.z - vVector.z)
	# overload the * operator
    def __mul__(self, number):
        return tVector3(self.x * number, self.y * number, self.z * number)
    # overload the / operator
    def __div__(self, number):
        return tVector3(self.x / number, self.y / number, self.z / number)
		
class CCamera(): # Our Camera
    def __init__(self): 
        self.mPos = tVector3(0.0, 0.0, 0.0)							
        self.mView = tVector3(0.0, 0.0, 0.0)							
        self.mUp = tVector3(0.0, 0.0, 0.0)				

    def Strafe_Camera(self, speed):
        vVector = self.mView - self.mPos # Get the view vector
        
        vOrthoVector = tVector3(0.0, 0.0, 0.0) # Orthogonal vector for the view vector
        vOrthoVector.x = -vVector.z
        vOrthoVector.z =  vVector.x
        # left positive cameraspeed and right negative -cameraspeed.
        self.mPos.x = self.mPos.x + vOrthoVector.x * speed
        self.mPos.z = self.mPos.z + vOrthoVector.z * speed
        self.mView.x = self.mView.x + vOrthoVector.x * speed
        self.mView.z = self.mView.z + vOrthoVector.z * speed
    
    def Rotate_Position(self, speed):
        vVector = self.mPos - self.mView

        self.mPos.z = self.mView.z + (math.sin(speed) * vVector.x) + (math.cos(speed) * vVector.z)
        self.mPos.x = self.mView.x + (math.cos(speed) * vVector.x) - (math.sin(speed) * vVector.z)
        return
    
    def Move_Camera(self, speed):
        vVector = self.mView - self.mPos	# Get the view vector
	
        # forward positive camera speed and backward negative camera speed.
        self.mPos.x = self.mPos.x + (vVector.x * speed)
        self.mPos.z = self.mPos.z + (vVector.z * speed)
        self.mView.x = self.mView.x + (vVector.x * speed)
        self.mView.z = self.mView.z + (vVector.z * speed)
	
    def Mouse_Move(self, wndWidth, wndHeight):
        mousePos = (0,0)	
        mid_x = wndWidth	
        mid_y = wndHeight
        angle_y  = 0.0				
        angle_z  = 0.0							

        pygame.mouse.get_pos(mousePos)
		
        if (mousePos.x == mid_x) and (mousePos.y == mid_y): 
            return

        pygame.mouse.set_pos(mid_x, mid_y);	# Set the mouse cursor in the center of the window						

        # Get the direction from the mouse cursor, set a resonable maneuvering speed
        angle_y = (mid_x - x) / 1000		
        angle_z = (mid_y - y) / 1000

        # The higher the value is the faster the camera looks around.
        self.mView.y = self.mView.y + angle_z * 2

        # limit the rotation around the x-axis
        if (self.mView.y > 3.5):
            self.mView.y = 3.5
        if (self.mView.y < 0.4):
            self.mView.y = 0.4
	
        Rotate_Position(-angle_y)
        return
		
    def Rotate_View(self, speed):
        vVector = self.mView - self.mPos	# Get the view vector

        self.mView.z = (self.mPos.z + math.sin(speed) * vVector.x + math.cos(speed) * vVector.z)
        self.mView.x = (self.mPos.x + math.cos(speed) * vVector.x - math.sin(speed) * vVector.z)
	
    def Position_Camera(self, pos_x, pos_y, pos_z, view_x, view_y, view_z, up_x, up_y, up_z):
        self.mPos = tVector3(pos_x, pos_y, pos_z ) # set position
        self.mView = tVector3(view_x, view_y, view_z) # set view
        self.mUp = tVector3(up_x, up_y, up_z) # set the up vector
        