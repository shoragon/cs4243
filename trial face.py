
import math
import numpy as np
import cv2 as cv2


class Vertex:

	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z
		
	def sum(a, b):
		return Vertex(a.x+b.x, a.y+b.y, a.z+b.z)
		
	def diff(a, b):
		return Vertex(a.x-b.x, a.y-b.y, a.z-b.z)
		
	def cross(a, b):
		return Vertex(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)
		
	def distance(a, b):
		x = math.pow(a.x-b.x, 2)
		y = math.pow(a.y-b.y, 2)
		z = math.pow(a.z-b.z, 2)
		return math.sqrt(x+y+z)
		
	def normalize(a):
		temp = math.sqrt(a.x*a.x+a.y*a.y+a.z*a.z)
		return Vertex(a.x/temp, a.y/temp, a.z/temp)
		
	def scale(a, v):
		return Vertex(a.x*v, a.y*v, a.z*v)
		
	def equal(a):
		return Vertex(a.x, a.y, a.z)
	
class Polygon:
	
	def __init__(self, newVertexList, newTexelList):
		# Create list to store all vertex
		self.VertexList = []
		for i in newVertexList:
			self.VertexList.append(i)
			
		# Create list to store all texel value
		self.TexelList = []
		for i in newTexelList:
			self.TexelList.append(i)
	
ver1 =(0,0)
ver2 =(1,0)
ver3 =(1,1)
ver4 =(0,1)
width = 800
height = 600
poly1 = Polygon([ver1, ver2, ver3, ver4], [])
each_frame = np.zeros((width,height,3),np.uint8)
average_color=(120,120,100)
pts = np.array([ver1,ver2,ver3,ver4],np.int32)
cv2.fillPoly(each_frame,[pts],average_color)
cv2.imshow('trial',each_frame)

