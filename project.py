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
xtri= [-0.2, 0.5,1.2,-0.2]
ytri= [1   , 1.5,  1,1]
ztri= [1   ,0.5 ,  1,1 ]
#triangle top-left
xtril=[-0.2, 0.5,-0.2,-0.2]
ytril=[1   , 1.5,   1,1]
ztril=[0   ,0.5 ,   1,0]
#triangle top-right
xtrir=[1.2,0.5,1.2,1.2]
ytrir=[1  ,1.5,  1,1]
ztrir=[0  ,0.5,  1,0]
#triangle top-back
xtrib=[1.2,0.5,-0.2,1.2]
ytrib=[1  ,1.5,  1,1]
ztrib=[0  ,0.5,  0,0 ]

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
xrectroofb=[-3 ,3  ,0   ]
yrectroofb=[0.6,0.6,1   ]
zrectroofb=[-1  ,-1  ,-0.5]
#triangle top-right
xrectroofr=[3 ,3  ,0     ]
yrectroofr=[0.6,0.6,1    ]
zrectroofr=[0  ,-1  ,-0.5]

#cylinder block behind
xcybf=[-1,1,1,-1]
ycybf=[0,0,1,1]
zcybf=[-1,-1,-1,-1]

xcybl=[-1,-1,-1,-1]
ycybl=[0,0,1,1]
zcybl=[-3,-1,-1,-3]

xcybr=[1,1,1,1]
ycybr=[0,0,1,1]
zcybr=[-1,-3,-3,-1]

xcybb=[-1,1,1,-1]
ycybb=[0,0,1,1]
zcybb=[-3,-3,-3,-3]

xcybt=[-1,-1,1,1]
ycybt=[1,1,1,1]
zcybt=[-3,-1,-1,-3]

#small rect blk on top of cyblk
xscybf=[-0.6,0.6,0.6,-0.6]
yscybf=[1,1,1.5,1.5]
zscybf=[-1,-1,-1,-1]

xscybl=[-0.6,-0.6,-0.6,-0.6]
yscybl=[1,1,1.5,1.5]
zscybl=[-3,-1,-1,-3]

xscybr=[0.6,0.6,0.6,0.6]
yscybr=[1,1,1.5,1.5]
zscybr=[-1,-3,-3,-1]

xscybb=[-0.6,0.6,0.6,-0.6]
yscybb=[1,1,1.5,1.5]
zscybb=[-3,-3,-3,-3]

xscybt=[-0.6,-0.6,0.6,0.6]
yscybt=[1.5,1.5,1.5,1.5]
zscybt=[-3,-1,-1,-3]
#many boxes building--------------------------
#main building
xmainboxf=[1,3,3,1]
ymainboxf=[0,0,3,3]
zmainboxf=[-5,-5,-5,-5]

xmainboxl=[1,1,1,1]
ymainboxl=[0,0,3,3]
zmainboxl=[-8,-5,-5,-8]

xmainboxr=[3,3,3,3]
ymainboxr=[0,0,3,3]
zmainboxr=[-5,-8,-8,-5]

xmainboxb=[1,3,3,1]
ymainboxb=[0,0,3,3]
zmainboxb=[-8,-8,-8,-8]

xmainboxt=[1,3,3,1]
ymainboxt=[3,3,3,3]
zmainboxt=[-5,-5,-8,-8]

#---------vertices--------------------------------------------
# block---------------------------------------
verts = [zip(x, y,z)]
verts1 = [zip(x1, y1,z1)]
verts2 = [zip(x2, y2,z2)]
verts3 = [zip(x3, y3,z3)]
verts4 = [zip(x4, y4,z4)]
verts5 = [zip(x5, y5,z5)]
# roof on block
vblkrooff=[zip(xtri,ytri,ztri)]
vblkroofl=[zip(xtril,ytril,ztril)]
vblkroofr=[zip(xtrir,ytrir,ztrir)]
vblkroofb=[zip(xtrib,ytrib,ztrib)]
#rectangle behind-----------------------------------------
vrectf=[zip(xrectf,yrectf,zrectf)]
vrectl=[zip(xrectl,yrectl,zrectl)]
vrectr=[zip(xrectr,yrectr,zrectr)]
vrectb=[zip(xrectb,yrectb,zrectb)]
vrectrooff=[zip(xrectrooff,yrectrooff,zrectrooff)]
vrectroofl=[zip(xrectroofl,yrectroofl,zrectroofl)]
vrectroofr=[zip(xrectroofr,yrectroofr,zrectroofr)]
vrectroofb=[zip(xrectroofb,yrectroofb,zrectroofb)]
#cylinder blk behind-------------------------------------
vcybf=[zip(xcybf,ycybf,zcybf)]
vcybl=[zip(xcybl,ycybl,zcybl)]
vcybr=[zip(xcybr,ycybr,zcybr)]
vcybb=[zip(xcybb,ycybb,zcybb)]
vcybt=[zip(xcybt,ycybt,zcybt)]

vscybf=[zip(xscybf,yscybf,zscybf)]
vscybl=[zip(xscybl,yscybl,zscybl)]
vscybr=[zip(xscybr,yscybr,zscybr)]
vscybb=[zip(xscybb,yscybb,zscybb)]
vscybt=[zip(xscybt,yscybt,zscybt)]

#many boxes building-------------------------------
vmainboxf=[zip(xmainboxf,ymainboxf,zmainboxf)]
vmainboxl=[zip(xmainboxl,ymainboxl,zmainboxl)]
vmainboxr=[zip(xmainboxr,ymainboxr,zmainboxr)]
vmainboxb=[zip(xmainboxb,ymainboxb,zmainboxb)]
vmainboxt=[zip(xmainboxt,ymainboxt,zmainboxt)]




fig = plt.figure()
ax = Axes3D(fig)
#front block-----------------------------------------
ax.add_collection3d(Poly3DCollection(verts), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts1), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts2), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts3), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts4), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(verts5), zs=0, zdir='x')
#roof of front block
ax.add_collection3d(Poly3DCollection(vblkrooff), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vblkroofl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vblkroofr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vblkroofb), zs=0, zdir='x')
#rectangle behind--------------------------------------
ax.add_collection3d(Poly3DCollection(vrectrooff), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectroofl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectroofr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectroofb), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vrectf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vrectb), zs=0, zdir='x')
#cylinder blk behind----------------------------------
ax.add_collection3d(Poly3DCollection(vcybf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vcybl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vcybr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vcybb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vcybt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vscybf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vscybl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vscybr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vscybb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vscybt), zs=0, zdir='x')
#many boxes building-------------------------------
ax.add_collection3d(Poly3DCollection(vmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vmainboxt), zs=0, zdir='x')

ax.set_xlabel('X')
ax.set_xlim3d(-4, 4)
ax.set_ylabel('Y')
ax.set_ylim3d(-4, 4)
ax.set_zlabel('Z')
ax.set_zlim3d(-4, 4)
plt.show()