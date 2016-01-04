# -*- coding: utf-8 -*-

__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

import vector

class CCamera(): # Our Camera
	def __init__(self): 
		self.mPos = vector.tVector3(0.0, 0.0, 0.0)							
		self.mView = vector.tVector3(0.0, 0.0, 0.0)							
		self.mUp = vector.tVector3(0.0, 0.0, 0.0)	
		self.mStrafe = vector.tVector3(0.0, 0.0, 0.0)
			
	def Position_Camera(self, pos_x, pos_y, pos_z, view_x, view_y, view_z, up_x, up_y, up_z):
		self.mPos = vector.tVector3(pos_x, pos_y, pos_z) # set position
		self.mView = vector.tVector3(view_x, view_y, view_z) # set view
		self.mUp = vector.tVector3(up_x, up_y, up_z) # set the up vector