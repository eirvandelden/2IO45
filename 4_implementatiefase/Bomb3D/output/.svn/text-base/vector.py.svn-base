
__author__ = "Leroy Bakker"

class tVector3():	# Extended 3D Vector Struct
	def __init__(self, new_x, new_y, new_z): # Init Constructor	 
		self.x, self.y, self.z = new_x, new_y, new_z
	# overload the + operator
	def __add__(self, vVector):
		return tVector3(vVector.x + self.x, vVector.y + self.y, vVector.z + self.z)
	# overload the - operator
	def __sub__(self, vVector):
		return tVector3(self.x - vVector.x, self.y - vVector.y, self.z - vVector.z)
	# overload the * operator
	def __mul__(self, number):
		return tVector3(self.x * number, self.y * number, self.z * number)
    # overload the / operator
	def __div__(self, number):
		return tVector3(self.x / number, self.y / number, self.z / number)