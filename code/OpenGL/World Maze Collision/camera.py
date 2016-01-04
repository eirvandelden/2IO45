from __future__ import division
import vector
import math
import math3D
import collision
import pygame
pygame.init()

CAMERASPEED = 0.15 # walking speed
ROTATESPEED = 1.5 # viewing speed factor

class CCamera(): # Our Camera
	def __init__(self): 
		self.mPos = vector.tVector3(0.0, 0.0, 0.0)							
		self.mView = vector.tVector3(0.0, 0.0, 0.0)							
		self.mUp = vector.tVector3(0.0, 0.0, 0.0)	
		self.mStrafe = vector.tVector3(0.0, 0.0, 0.0)
		self.mRadius = 1
		
	def Strafe_Camera(self, speed):
		vVector = self.mView - self.mPos # Get the view vector
        
		vOrthoVector = vector.tVector3(0.0, 0.0, 0.0) # Orthogonal vector for the view vector
		vOrthoVector.x = -vVector.z
		vOrthoVector.z =  vVector.x
		# left positive cameraspeed and right negative -cameraspeed.
		self.mPos.x = self.mPos.x + vOrthoVector.x * speed
		self.mPos.z = self.mPos.z + vOrthoVector.z * speed
		self.mView.x = self.mView.x + vOrthoVector.x * speed
		self.mView.z = self.mView.z + vOrthoVector.z * speed
		
	def Mouse_Move(self, wndWidth, wndHeight):
		mid_x = wndWidth / 2	
		mid_y = wndHeight / 2
		angle_y  = 0.0
		angle_z  = 0.0
		currentRotX = 0.0
	
		mousepos = pygame.mouse.get_pos() # Get the mouse cursor 2D x,y position					
	
		if (mousepos[0] == mid_x) and (mousepos[1] == mid_y): return

		pygame.mouse.set_pos(mid_x, mid_y) # Set the mouse cursor in the center of the window						

		# Get the direction from the mouse cursor, set a resonable maneuvering speed
		angle_y = (mid_x - mousepos[0]) / 1000		
		angle_z = (mid_y - mousepos[1]) / 1000
			
		currentRotX = currentRotX - angle_z  

		# If the current rotation (in radians) is greater than 1.0, we want to cap it.
		if(currentRotX > 1.0): currentRotX = 1.0
		# Check if the rotation is below -1.0, if so we want to make sure it doesn't continue
		elif(currentRotX < -1.0): currentRotX = -1.0
		# Otherwise, we can rotate the view around our position
		else:
			# To find the axis we need to rotate around for up and down
			# movements, we need to get a perpendicular vector from the
			# camera's view vector and up vector.  This will be the axis.
			vAxis = math3D.Cross(self.mView - self.mPos, self.mUp)
			vAxis = math3D.Normalize(vAxis)

		# Rotate around our perpendicular axis and along the y-axis
		#self.Rotate_View(angle_z, vAxis.x, vAxis.y, vAxis.z) # up and down view
		self.Rotate_View(angle_y * ROTATESPEED, 0, 1, 0) # left and right view

		# self.Rotate_Position(-angle_y)
    
	def Rotate_Position(self, speed):
		vVector = self.mPos - self.mView

		self.mPos.z = self.mView.z + (math.sin(speed) * vVector.x) + (math.cos(speed) * vVector.z)
		self.mPos.x = self.mView.x + (math.cos(speed) * vVector.x) - (math.sin(speed) * vVector.z)
    
	def Move_Camera(self, speed):
		vVector = self.mView - self.mPos	# Get the view vector
	
		# forward positive camera speed and backward negative camera speed.
		self.mPos.x = self.mPos.x + (vVector.x * speed)
		self.mPos.z = self.mPos.z + (vVector.z * speed)
		self.mView.x = self.mView.x + (vVector.x * speed)
		self.mView.z = self.mView.z + (vVector.z * speed)
	
	def Rotate_View(self, angle, x, y, z):
		vNewView = vector.tVector3(0,0,0)
		# Get the view vector (The direction we are facing)
		vView = self.mView - self.mPos		

		# Calculate the sine and cosine of the angle once
		cosTheta = math.cos(angle)
		sinTheta = math.sin(angle)

		# Find the new x position for the new rotated point
		vNewView.x = (cosTheta + (1 - cosTheta) * x * x) * vView.x
		vNewView.x = vNewView.x + ((1 - cosTheta) * x * y - z * sinTheta) * vView.y
		vNewView.x = vNewView.x + ((1 - cosTheta) * x * z + y * sinTheta) * vView.z

		# Find the new y position for the new rotated point
		vNewView.y = ((1 - cosTheta) * x * y + z * sinTheta) * vView.x
		vNewView.y = vNewView.y + (cosTheta + (1 - cosTheta) * y * y) * vView.y
		vNewView.y = vNewView.y + ((1 - cosTheta) * y * z - x * sinTheta) * vView.z

		# Find the new z position for the new rotated point
		vNewView.z = ((1 - cosTheta) * x * z - y * sinTheta) * vView.x
		vNewView.z = vNewView.z + ((1 - cosTheta) * y * z + x * sinTheta) * vView.y
		vNewView.z = vNewView.z + (cosTheta + (1 - cosTheta) * z * z) * vView.z

		# Now we just add the newly rotated vector to our position to set
		# our new rotated view of our camera.
		self.mView = self.mPos + vNewView
	
	def Position_Camera(self, pos_x, pos_y, pos_z, view_x, view_y, view_z, up_x, up_y, up_z):
		self.mPos = vector.tVector3(pos_x, pos_y, pos_z) # set position
		self.mView = vector.tVector3(view_x, view_y, view_z) # set view
		self.mUp = vector.tVector3(up_x, up_y, up_z) # set the up vector
		
	def CheckCameraCollision(self, pVertices, numOfVerts):
		# This function is pretty much a direct rip off of SpherePolygonCollision()
		# We needed to tweak it a bit though, to handle the collision detection once 
		# it was found, along with checking every triangle in the list if we collided.  
		# pVertices is the world data. If we have space partitioning, we would pass in 
		# the vertices that were closest to the camera. What happens in this function 
		# is that we go through every triangle in the list and check if the camera's 
		# sphere collided with it.  If it did, we don't stop there.  We can have 
		# multiple collisions so it's important to check them all.  One a collision 
		# is found, we calculate the offset to move the sphere off of the collided plane.

		# Go through all the triangles
		for i in range(0,numOfVerts,3):
			# Store of the current triangle we testing
			vTriangle = []
			vTriangle.append(pVertices[i])
			vTriangle.append(pVertices[i+1])
			vTriangle.append(pVertices[i+2])

			# 1) STEP ONE - Finding the sphere's classification
		
			# We want the normal to the current polygon being checked
			vNormal = math3D.Normal(vTriangle)

			# This will store the distance our sphere is from the plane
			distance = 0.0

			# This is where we determine if the sphere is in FRONT, BEHIND, or INTERSECTS the plane
			classification = collision.ClassifySphere(self.mPos, vNormal, vTriangle[0], self.mRadius, distance)

			# If the sphere intersects the polygon's plane, then we need to check further
			if(classification == collision.INTERSECTS): 
				# 2) STEP TWO - Finding the psuedo intersection point on the plane

				# Now we want to project the sphere's center onto the triangle's plane
				vOffset = vNormal * distance

				# Once we have the offset to the plane, we just subtract it from the center
				# of the sphere.  "vIntersection" is now a point that lies on the plane of the triangle.
				vIntersection = self.mPos - vOffset

				# 3) STEP THREE - Check if the intersection point is inside the triangles perimeter

				# We first check if our intersection point is inside the triangle, if not,
				# the algorithm goes to step 4 where we check the sphere again the polygon's edges.

				# We do one thing different in the parameters for EdgeSphereCollision though.
				# Since we have a bulky sphere for our camera, it makes it so that we have to 
				# go an extra distance to pass around a corner. This is because the edges of 
				# the polygons are colliding with our peripheral view (the sides of the sphere).  
				# So it looks likes we should be able to go forward, but we are stuck and considered 
				# to be colliding.  To fix this, we just pass in the radius / 2.  Remember, this
				# is only for the check of the polygon's edges.  It just makes it look a bit more
				# realistic when colliding around corners.  Ideally, if we were using bounding box 
				# collision, cylinder or ellipses, this wouldn't really be a problem.
				
				inPolygon = collision.InsidePolygon(vIntersection, vTriangle, 3)
				camColEdge = collision.EdgeSphereCollision(self.mPos, vTriangle, 3, self.mRadius / 2)
				if (inPolygon or camColEdge):
					# If we get here, we have collided!  To handle the collision detection
					# all it takes is to find how far we need to push the sphere back.
					# GetCollisionOffset() returns us that offset according to the normal,
					# camerspeed (step size), and current distance the center of the sphere is from the plane.
					vOffset = collision.GetCollisionOffset(vNormal, CAMERASPEED, distance)

					# Now that we have the offset, we want to ADD it to the position and
					# view vector in our camera.  This pushes us back off of the plane.  We
					# don't see this happening because we check collision before we render
					# the scene.
					self.mPos = self.mPos + vOffset
					self.mView = self.mView + vOffset
					
