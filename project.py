from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
#Front face
x = [0,1,1,0]
y = [0,0,1,1]
z = [1,1,1,1]
#Top
x1 = [0,0,1,1]
y1 = [1,1,1,1]
z1 = [1,0,0,1]
#Right
x2 = [1,1,1,1]
y2 = [1,0,0,1]
z2 = [1,1,0,0]
#Left face
x3 = [0,0,0,0]
y3 = [0,1,1,0]
z3 = [1,1,0,0]
#Back Face
x4 = [0,1,1,0]
y4 = [0,0,1,1]
z4 = [0,0,0,0]
#Bottom Face
x5 = [0,1,1,0]
y5 = [0,0,0,0]
z5 = [1,1,0,0]
verts = [zip(x, y,z)]
verts1 = [zip(x1, y1,z1)]
verts2 = [zip(x2, y2,z2)]
verts3 = [zip(x3, y3,z3)]
verts4 = [zip(x4, y4,z4)]
verts5 = [zip(x5, y5,z5)]

fig = plt.figure()
ax = Axes3D(fig)
ax.add_collection3d(Poly3DCollection(verts), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts1), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts2), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts3), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts4), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts5), zs=0, zdir='x')
ax.set_xlabel('X')
ax.set_xlim3d(0, 2)
ax.set_ylabel('Y')
ax.set_ylim3d(0, 2)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 2)
plt.show()