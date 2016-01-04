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

#	This returns the normal of a polygon (The direction the polygon is facing)
def Normal(vPolygon):					
	# Get 2 vectors from the polygon (2 sides), Remember the order!
	vVector1 = vPolygon[2] - vPolygon[0]
	vVector2 = vPolygon[1] - vPolygon[0]

	vNormal = Cross(vVector1, vVector2) # Take the cross product of our 2 vectors to get a perpendicular vector

	# Now we have a normal, but it's at a strange length, so let's make it length 1.

	vNormal = Normalize(vNormal) # Use our function we created to normalize the normal (Makes it a length of one)

	return vNormal # Return our normal at our desired length

# This returns the distance between 2 3D points
def Distance(vPoint1, vPoint2):
	p1, p2 = vPoint1, vPoint2
	# This is the classic formula used in beginning algebra to return the
	# distance between 2 points.  Since it's 3D, we just add the z dimension:
	distance = math.sqrt( (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y) + (p2.z - p1.z) * (p2.z - p1.z) )

	# Return the distance between the 2 points
	return distance
	
# This returns the point on the line vA-vB that is closest to the point vPoint
def ClosestPointOnLine(vA, vB, vPoint):
	# Create the vector from end point vA to our point vPoint.
	vVector1 = vPoint - vA

	# Create a normalized direction vector from end point vA to end point vB
	vVector2 = Normalize(vB - vA)

	# Use the distance formula to find the distance of the line segment (or magnitude)
	d = Distance(vA, vB)

	# Using the dot product, we project the vVector1 onto the vector vVector2.
	# This essentially gives us the distance from our projected vector from vA.
	t = Dot(vVector2, vVector1)

	# If our projected distance from vA, "t", is less than or equal to 0, it must
	# be closest to the end point vA.  We want to return this end point.
	if (t <= 0): return vA

	# If our projected distance from vA, "t", is greater than or equal to the magnitude
	# or distance of the line segment, it must be closest to the end point vB.  So, return vB.
	if (t >= d): return vB
 
	# Here we create a vector that is of length t and in the direction of vVector2
	vVector3 = vVector2 * t

	# To find the closest point on the line segment, we just add vVector3 to the original
	# end point vA.  
	vClosestPoint = vA + vVector3

	# Return the closest point on the line segment
	return vClosestPoint
	
# This returns the distance between a plane and the origin
def PlaneDistance(vNormal, vPoint):
	# Use the plane equation to find the distance (Ax + By + Cz + D = 0)  We want to find D.
	# So, we come up with D = -(Ax + By + Cz)
	# Basically, the negated dot product of the normal of the plane and the point. (More about the dot product in another tutorial)
	distance = - ((vNormal.x * vPoint.x) + (vNormal.y * vPoint.y) + (vNormal.z * vPoint.z))

	return distance # Return the distance
	
# This checks if a line and a plane intersect
def IntersectedPlane(vPoly, vLine, vNormal, originDistance): # vPoly, vLine is a list of tVector3
	vNormal = Normal(vPoly) # We need to get the normal of our plane to go any further

	# Let's find the distance our plane is from the origin.  We can find this value
	# from the normal to the plane (polygon) and any point that lies on that plane (Any vertex)
	originDistance = PlaneDistance(vNormal, vPoly[0])

	# Get the distance from point1 from the plane using: Ax + By + Cz + D = (The distance from the plane)
	distance1 = ((vNormal.x * vLine[0].x) +	(vNormal.y * vLine[0].y) + (vNormal.z * vLine[0].z)) + originDistance
	
	# Get the distance from point2 from the plane using Ax + By + Cz + D = (The distance from the plane)
	distance2 = ((vNormal.x * vLine[1].x) + (vNormal.y * vLine[1].y) + (vNormal.z * vLine[1].z)) + originDistance

	# Now that we have 2 distances from the plane, if we multiply them we either
	# get a positive or negative number.  If it's a negative number, that means we collided!
	# This is because the 2 points must be on either side of the plane (IE. -1 * 1 = -1).

	if(distance1 * distance2 >= 0): return False
	# Check to see if both point's distances are both negative or both positive
	# Return false if each point has the same sign.  -1 and 1 would mean each point is on either side of the plane.  -1 -2 or 3 4 wouldn't...
					
	return True # The line intersected the plane, Return TRUE

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
	
# This returns an intersection point of a polygon and a line (assuming it intersects the plane)
def IntersectionPoint(vNormal, vLine, distance):
	Numerator, Denominator, dist = 0.0, 0.0, 0.0

	# 1)  First we need to get the vector of our line, Then normalize it so it's a length of 1
	vLineDir = vLine[1] - vLine[0] # Get the Vector of the line
	vLineDir = Normalize(vLineDir) # Normalize the lines vector


	# 2) Use the plane equation (distance = Ax + By + Cz + D) to find the 
	# distance from one of our points to the plane.
	Numerator = -(vNormal.x * vLine[0].x + vNormal.y * vLine[0].y + vNormal.z * vLine[0].z + distance)

	# 3) If we take the dot product between our line vector and the normal of the polygon,
	Denominator = Dot(vNormal, vLineDir)		# Get the dot product of the line's vector and the normal of the plane
				  
	# Since we are using division, we need to make sure we don't get a divide by zero error
	# If we do get a 0, that means that there are INFINATE points because the the line is
	# on the plane (the normal is perpendicular to the line - (Normal.Vector = 0)).  
	# In this case, we should just return any point on the line.

	if(Denominator == 0.0): return vLine[0] 
	# Check so we don't divide by zero
	# Return an arbitrary point on the line

	dist = Numerator / Denominator # Divide to get the multiplying (percentage) factor
	
	# Now, like we said above, we times the dist by the vector, then add our arbitrary point.
	vPoint.x = (vLine[0].x + (vLineDir.x * dist))
	vPoint.y = (vLine[0].y + (vLineDir.y * dist))
	vPoint.z = (vLine[0].z + (vLineDir.z * dist))

	return vPoint # Return the intersection point
	
