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
#triangle top-front
xTri= [-0.2, 0.5,1.2]
yTri= [1   , 1.5,  1]
zTri= [0   ,0.5 ,  0]
#triangle top-left
xtril=[-0.2, 0.5,-0.2]
ytril=[1   , 1.5,   1]
ztril=[0   ,0.5 ,   1]
#triangle top-right
xtrir=[1.2,0.5,1.2]
ytrir=[1  ,1.5,  1]
ztrir=[0  ,0.5,  1]
#triangle top-back
xtrib=[1.2,0.5,-0.2]
ytrib=[1  ,1.5,  1]
ztrib=[1  ,0.5,  1]

#rectangular block behind-front
xrectf=[-3 ,-3,3,3  ]
yrectf=[0.6,0 ,0,0.6]
zrectf=[0  ,0 ,0,0  ]
#rectangular block behind-left
xrectl=[-3 ,-3,-3,-3 ]
yrectl=[0.6,0 ,0,0.6]
zrectl=[0  ,0 ,-1,-1 ]
#rectangular block behind-back
xrectb=[-3 ,-3,3,3  ]
yrectb=[0.6,0 ,0,0.6]
zrectb=[-1 ,-1,-1,-1]
#rectangular block behind-right
xrectr=[ 3 ,3 , 3, 3 ]
yrectr=[0.6,0 ,0,0.6 ]
zrectr=[0  ,0 ,-1,-1 ]
#triangle top-front
xrectrooff=[-3 ,3  ,0   ]
yrectrooff=[0.6,0.6,1   ]
zrectrooff=[0  ,0  ,-0.5]
#triangle top-left
xrectroofl=[-3 ,-3  ,0   ]
yrectroofl=[0.6,0.6,1    ]
zrectroofl=[0  ,-1  ,-0.5]
#triangle top-back
xrectroofl=[-3 ,3  ,0   ]
yrectroofl=[0.6,0.6,1   ]
zrectroofl=[-1  ,-1  ,-0.5]
#triangle top-right
xrectroofl=[3 ,3  ,0     ]
yrectroofl=[0.6,0.6,1    ]
zrectroofl=[0  ,-1  ,-0.5]


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
ax.set_xlim3d(-4, 4)
ax.set_ylabel('Y')
ax.set_ylim3d(0, 2)
ax.set_zlabel('Z')
ax.set_zlim3d(0, 2)
plt.show()