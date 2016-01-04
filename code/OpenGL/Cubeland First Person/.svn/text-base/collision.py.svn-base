import vector # Needed for 3D vector
import math # Needed for sqrt
import math3D # Needed for 3D math calculations

BEHIND = 0
INTERSECTS = 1
FRONT = 2

# This returns true if the intersection point is inside of the polygon, false otherwise
def InsidePolygon(vIntersection, Poly, verticeCount):
	MATCH_FACTOR = 0.99 # Used to cover up the error in floating point
	angle = 0.0 # Initialize the angle
	
	for i in range(0, verticeCount): # Go in a circle to each vertex and get the angle between	
		vA = Poly[i] - vIntersection # Subtract the intersection point from the current vertex
		# Subtract the point from the next vertex
		vB = Poly[(i + 1) % verticeCount] - vIntersection
												
		angle = angle + math3D.AngleBetweenVectors(vA, vB) # Find the angle between the 2 vectors and add them all up as we go along
											
	if(angle >= (MATCH_FACTOR * (2.0 * math.pi)) ): # If the angle is greater than 2 PI, (360 degrees)
		return True # The point is inside of the polygon
		
	return False # If you get here, it obviously wasn't inside the polygon, so Return FALSE
	
# Use this function to test collision between a line and polygon
def IntersectedPolygon(vPoly, vLine, verticeCount):
	originDistance = 0

	# First, make sure our line intersects the plane
	if( not(math3D.IntersectedPlane(vPoly, vLine, vNormal, originDistance))):
		return False

	# Now that we have our normal and distance passed back from IntersectedPlane(), 
	# we can use it to calculate the intersection point.  
	vIntersection = math3D.IntersectionPoint(vNormal, vLine, originDistance)

	# Now that we have the intersection point, we need to test if it's inside the polygon.
	if(InsidePolygon(vIntersection, vPoly, verticeCount)):
		return True # We collided! Return success

	return False # There was no collision, so return false
	
# This function classifies a sphere according to a plane. (BEHIND, in FRONT, or INTERSECTS)
def ClassifySphere(vCenter, vNormal, vPoint, radius, distance):
	# First we need to find the distance our polygon plane is from the origin.
	d = math3D.PlaneDistance(vNormal, vPoint)

	# Here we use the famous distance formula to find the distance the center point
	# of the sphere is from the polygon's plane.  
	distance = (vNormal.x * vCenter.x + vNormal.y * vCenter.y + vNormal.z * vCenter.z + d)

	# If the absolute value of the distance we just found is less than the radius, 
	# the sphere intersected the plane.
	if(math3D.Absolute(distance) < radius): return INTERSECTS
	
	# Else, if the distance is greater than or equal to the radius, the sphere is
	# completely in FRONT of the plane.
	elif(distance >= radius): return FRONT
	
	# If the sphere isn't intersecting or in FRONT of the plane, it must be BEHIND
	return BEHIND
	
# This function takes the sphere's center, the polygon's vertices, the vertex count
# and the radius of the sphere.  We will return true if the sphere
# is intersecting any of the edges of the polygon.  
def EdgeSphereCollision(vCenter, vPolygon, vertexCount, radius):

	# Go through all of the vertices in the polygon
	for i in range(0,vertexCount):
		# This returns the closest point on the current edge to the center of the sphere.
		vPoint = math3D.ClosestPointOnLine(vPolygon[i], vPolygon[(i + 1) % vertexCount], vCenter)
		
		# Now, we want to calculate the distance between the closest point and the center
		distance = math3D.Distance(vPoint, vCenter)

		# If the distance is less than the radius, there must be a collision so return true
		if (distance < radius): return True

	# The was no intersection of the sphere and the edges of the polygon
	return False
	
# This returns true if the sphere is intersecting with the polygon, false otherwise
def SpherePolygonCollision(vPolygon, vCenter, vertexCount, radius):
	# 1) STEP ONE - Finding the sphere's classification
	
	# Let's use our Normal() function to return us the normal to this polygon
	vNormal = math3D.Normal(vPolygon)

	# This will store the distance our sphere is from the plane
	distance = 0.0

	# This is where we determine if the sphere is in FRONT, BEHIND, or INTERSECTS the plane
	classification = math3D.ClassifySphere(vCenter, vNormal, vPolygon[0], radius, distance)

	# If the sphere intersects the polygon's plane, then we need to check further
	if (classification == INTERSECTS):
		# 2) STEP TWO - Finding the psuedo intersection point on the plane

		# Now we want to project the sphere's center onto the polygon's plane
		vOffset = vNormal * distance

		# Once we have the offset to the plane, we just subtract it from the center
		# of the sphere.  "vPosition" now a point that lies on the plane of the polygon.
		vPosition = vCenter - vOffset

		# 3) STEP THREE - Check if the intersection point is inside the polygons perimeter

		# If the intersection point is inside the perimeter of the polygon, it returns true.
		# We pass in the intersection point, the list of vertices and vertex count of the poly.
		if (InsidePolygon(vPosition, vPolygon, 3)): return True	# We collided!
		else:
			# 4) STEP FOUR - Check the sphere intersects any of the polygon's edges

			# If we get here, we didn't find an intersection point in the perimeter.
			# We now need to check collision against the edges of the polygon.
			if (EdgeSphereCollision(vCenter, vPolygon, vertexCount, radius)):
				return True	# We collided!
	# If we get here, there is obviously no collision
	return False

# This function returns the offset in which the sphere needs to move in order to not intersect the plane	
def GetCollisionOffset(vNormal, radius, distance):
	vOffset = vector.tVector3(0, 0, 0)

	# Once we find if a collision has taken place, we need to make sure the sphere
	# doesn't move into the wall.  In our app, the position will actually move into
	# the wall, but we check our collision detection before we render the scene, which
	# eliminates the bounce back effect it would cause.  The question is, how do we
	# know which direction to move the sphere back?  In our collision detection, we
	# account for collisions on both sides of the polygon.  Usually, you just need
	# to worry about the side with the normal vector and positive distance.  If 
	# you don't want to back face cull and have 2 sided planes, I check for both sides.

	# Let me explain the math that is going on here.  First, we have the normal to
	# the plane, the radius of the sphere, as well as the distance the center of the
	# sphere is from the plane.  In the case of the sphere colliding in the front of
	# the polygon, we can just subtract the distance from the radius, then multiply
	# that new distance by the normal of the plane.  This projects that leftover
	# distance along the normal vector.  For instance, say we have these values:
	
	#	vNormal = (1, 0, 0)		radius = 5		distance = 3

	# If we subtract the distance from the radius we get: (5 - 3 = 2)
	# The number 2 tells us that our sphere is over the plane by a distance of 2.
	# So basically, we need to move the sphere back 2 units.  How do we know which
	# direction though?  This part is easy, we have a normal vector that tells us the
	# direction of the plane.  
	# If we multiply the normal by the left over distance we get:  (2, 0, 0)
	# This new offset vectors tells us which direction and how much to move back.
	# We then subtract this offset from the sphere's position, giving is the new
	# position that is lying right on top of the plane.  Ba da bing!
	# If we are colliding from behind the polygon (not usual), we do the opposite
	# signs as seen below:
	
	# If our distance is greater than zero, we are in front of the polygon
	if (distance > 0):
		# Find the distance that our sphere is overlapping the plane, then
		# find the direction vector to move our sphere.
		distanceOver = radius - distance
		vOffset = vNormal * distanceOver
	else: # Else colliding from behind the polygon
		# Find the distance that our sphere is overlapping the plane, then
		# find the direction vector to move our sphere.
		distanceOver = radius + distance
		vOffset = vNormal * -distanceOver

	# There is one problem with check for collisions behind the polygon, and that
	# is if you are moving really fast and your center goes past the front of the
	# polygon, it will then assume you were colliding from behind and not let
	# you back in.  Most likely you will take out the if / else check, but I
	# figured I would show both ways in case someone didn't want to back face cull.

	# Return the offset we need to move back to not be intersecting the polygon.
	return vOffset