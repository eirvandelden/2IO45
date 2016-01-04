# -*- coding: utf-8 -*-

__author__ = "OGO 3.1 Groep 2"
__version__ = "0.1"
__license__ = "Public Domain"

import math # Needed for sqrt
import vector # Needed for 3D vector

def Absolute(num):
	if(num < 0): return (0 - num)
	return num

def Cross(vVector1,vVector2):
	vNormal = vector.tVector3(0,0,0) # The vector to hold the cross product

	# The X value for the vector is:  (V1.y * V2.z) - (V1.z * V2.y)
	vNormal.x = ((vVector1.y * vVector2.z) - (vVector1.z * vVector2.y))
														
	# The Y value for the vector is:  (V1.z * V2.x) - (V1.x * V2.z)
	vNormal.y = ((vVector1.z * vVector2.x) - (vVector1.x * vVector2.z))
														
	# The Z value for the vector is:  (V1.x * V2.y) - (V1.y * V2.x)
	vNormal.z = ((vVector1.x * vVector2.y) - (vVector1.y * vVector2.x))

	return vNormal # Return the cross product (Direction the polygon is facing - Normal)
	
def Dot(vVector1, vVector2):
	# The dot product is this equation: V1.V2 = (V1.x * V2.x  +  V1.y * V2.y  +  V1.z * V2.z)
	# In math terms, it looks like this:  V1.V2 = ||V1|| ||V2|| cos(theta)
	return ( (vVector1.x * vVector2.x) + (vVector1.y * vVector2.y) + (vVector1.z * vVector2.z) )

def Magnitude(vNormal):
	# This will give us the magnitude or "Norm" as some say, of our normal.
	# Here is the equation:  magnitude = sqrt(V.x^2 + V.y^2 + V.z^2)  Where V is the vector
	return math.sqrt( (vNormal.x * vNormal.x) + (vNormal.y * vNormal.y) + (vNormal.z * vNormal.z) )
	
def Normalize(vNormal):
	magnitude = Magnitude(vNormal) # Get the magnitude of our normal

	# Now that we have the magnitude, we can divide our normal by that magnitude.
	# That will make our normal a total length of 1.  This makes it easier to work with too.

	vNormal.x = vNormal.x / magnitude # Divide the X value of our normal by it's magnitude
	vNormal.y = vNormal.y / magnitude # Divide the Y value of our normal by it's magnitude
	vNormal.z = vNormal.z / magnitude # Divide the Z value of our normal by it's magnitude

	# Finally, return our normalized normal.

	return vNormal # Return the new normal of length 1

# This returns the distance between 2 3D points
def Distance(vPoint1, vPoint2):
	p1, p2 = vPoint1, vPoint2
	# This is the classic formula used in beginning algebra to return the
	# distance between 2 points.  Since it's 3D, we just add the z dimension:
	distance = math.sqrt( (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y) + (p2.z - p1.z) * (p2.z - p1.z) )

	# Return the distance between the 2 points
	return distance
	
# This returns the angle between 2 vectors
def AngleBetweenVectors(Vector1, Vector2):						
	# Get the dot product of the vectors
	dotProduct = Dot(Vector1, Vector2)

	# Get the product of both of the vectors magnitudes
	vectorsMagnitude = Magnitude(Vector1) * Magnitude(Vector2)

	# Get the angle in radians between the 2 vectors
	angle = math.acos( dotProduct / vectorsMagnitude )

	# Here we make sure that the angle is not a -1.#IND0000000 number, which means indefinate
	if(str(angle) == "nan"): return 0
	
	# Return the angle in radians
	return angle