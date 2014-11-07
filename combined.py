from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
#B1 Front Face 
x01=[4,4,7,7]
y01=[0,2,2,0]
z01=[9,9,9,9]
#B1 Left Face
x02=[4,4,4,4]
y02=[0,2,2,0]
z02=[5,5,9,9]
#B1 Right Face
x03=[7,7,7,7]
y03=[0,2,2,0]
z03=[5,5,9,9]
#B1 Back Face
x04=[4,4,7,7]
y04=[0,2,2,0]
z04=[5,5,5,5]
#B1 Roof
#Roof Front face
xRF01=[4,5.5,7]
yRF01=[2,3,2]
zRF01=[9,7,9]
#Roof Left Face
xRF02=[4,5.5,4]
yRF02=[2,3,2]
zRF02=[5,7,9]
#Roof Back Face
xRF03=[4,5.5,7]
yRF03=[2,3,2]
zRF03=[5,7,5]
#Roof Right Face
xRF04=[7,5.5,7]
yRF04=[2,3,2]
zRF04=[5,7,9]



#B22 Front Face 
x11=[4,4,7,7]
y11=[0,2,2,0]
z11=[4,4,4,4]
#B22 Left Face
x12=[4,4,4,4]
y12=[0,2,2,0]
z12=[3,3,4,4]
#B22 Right Face
x13=[7,7,7,7]
y13=[0,2,2,0]
z13=[3,3,4,4]
#B22 Back Face
x14=[4,4,7,7]
y14=[0,2,2,0]
z14=[3,3,3,3]
#B22 Roof
#Roof Front face
xRF11=[4,5.5,7]
yRF11=[2,3,2]
zRF11=[4,3.5,4]
#Roof Left Face
xRF12=[4,5.5,4]
yRF12=[2,3,2]
zRF12=[3,3.5,4]
#Roof Back Face
xRF13=[4,5.5,7]
yRF13=[2,3,2]
zRF13=[3,3.5,3]
#Roof Right Face
xRF14=[7,5.5,7]
yRF14=[2,3,2]
zRF14=[3,3.5,4]



#B2 Front Face 
x21=[4,4,7,7]
y21=[0,2,2,0]
z21=[3,3,3,3]
#B2 Left Face
x22=[4,4,4,4]
y22=[0,2,2,0]
z22=[3,3,-3,-3]
#B2 Right Face
x23=[7,7,7,7]
y23=[0,2,2,0]
z23=[3,3,-3,-3]
#B2 Back Face
x24=[4,4,7,7]
y24=[0,2,2,0]
z24=[-3,-3,-3,-3]
#B2 Roof
#Roof Front face
xRF21=[4,5.5,7]
yRF21=[2,3,2]
zRF21=[3,0,3]
#Roof Left Face
xRF22=[4,5.5,4]
yRF22=[2,3,2]
zRF22=[-3,0,3]
#Roof Back Face
xRF23=[4,5.5,7]
yRF23=[2,3,2]
zRF23=[-3,0,-3]
#Roof Right Face
xRF24=[7,5.5,7]
yRF24=[2,3,2]
zRF24=[-3,0,3]



#B3 Part 1 Front Face 
x31=[1,1,3,3]
y31=[0.5,2,2,0.5]
z31=[2,2,2,2]
#B3 Part 1 Left Face
x32=[1,1,1,1]
y32=[0.5,2,2,0.5]
z32=[2,2,1,1]
#B3 Part 1 Right Face
x33=[3,3,3,3]
y33=[0.5,2,2,0.5]
z33=[2,2,1,1]
#B3 Part 1 Back Face
x34=[1,1,3,3]
y34=[0.5,2,2,0.5]
z34=[1,1,1,1]
#B3 Part 1 Top
x35=[1,1,3,3]
y35=[2,2,2,2]
z35=[1,2,2,1]



#B3 Part 2 Front Face 
x41=[3,3,3.5,3.5]
y41=[0.5,2,2,0]
z41=[2,2,2,2]
#B3 Part 2 Left Face
x42=[3,3,3,3]
y42=[0.5,2,2,0.5]
z42=[2,2,1,1]
#B3 Part 2 Right Face
x43=[3.5,3.5,3.5,3.5]
y43=[0,2,2,0]
z43=[2,2,1,1]
#B3 Part 2 Back Face
x44=[3,3,3.5,3.5]
y44=[0.5,2,2,0]
z44=[1,1,1,1]
#B3 Part 2 Top
x45=[3,3,3.5,3.5]
y45=[2,2,2,2]
z45=[1,2,2,1]


#B3 Part 3 Front Face 
x51=[3.5,3.5,4,4]
y51=[0,2,1.5,0]
z51=[2,2,2,2]
#B3 Part 3 Left Face
x52=[3.5,3.5,3.5,3.5]
y52=[0,2,2,0]
z52=[2,2,1,1]
#B3 Part 3 Right Face
x53=[4,4,4,4]
y53=[0,1.5,1.5,0]
z53=[2,2,1,1]
#B3 Part 3 Back Face
x54=[3.5,3.5,4,4]
y54=[0,2,1.5,0]
z54=[1,1,1,1]
#B3 Part 3 Top
x55=[3.5,3.5,4,4]
y55=[2,2,1.5,1.5]
z55=[1,2,2,1]



#B4 Front Face 
x61=[3.5,3.5,4,4]
y61=[0,0.5,0.5,0]
z61=[5,5,5,5]
#B4 Left Face
x62=[3.5,3.5,3.5,3.5]
y62=[0,0.5,0.5,0]
z62=[5,5,4,4]
#B4 Right Face
x63=[4,4,4,4]
y63=[0,0.5,0.5,0]
z63=[5,5,4,4]
#B4 Back Face
x64=[3.5,3.5,4,4]
y64=[0,0.5,0.5,0]
z64=[4,4,4,4]



#Grass
x75=[-10,-10,10,10]
y75=[0.01,0.01,0.01,0.01]
z75=[-10,10,10,-10]

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

#front left blk
xflmainboxf=[1,2,2,1]
yflmainboxf=[0,0,2.5,2.5]
zflmainboxf=[-4,-4,-4,-4]

xflmainboxl=[1,1,1,1]
yflmainboxl=[0,0,2.5,2.5]
zflmainboxl=[-5,-4,-4,-5]

xflmainboxr=[2,2,2,2]
yflmainboxr=[0,0,2.5,2.5]
zflmainboxr=[-4,-5,-5,-4]

xflmainboxb=[1,2,2,1]
yflmainboxb=[0,0,2.5,2.5]
zflmainboxb=[-5,-5,-5,-5]

xflmainboxt=[1,2,2,1]
yflmainboxt=[2.5,2.5,2.5,2.5]
zflmainboxt=[-4,-4,-5,-5]

#front right box
xfrmainboxf=[2,3,3,2]
yfrmainboxf=[0,0,2,2]
zfrmainboxf=[-4,-4,-4,-4]

xfrmainboxl=[2,2,2,2]
yfrmainboxl=[0,0,2,2]
zfrmainboxl=[-5,-4,-4,-5]

xfrmainboxr=[3,3,3,3]
yfrmainboxr=[0,0,2,2]
zfrmainboxr=[-4,-5,-5,-4]

xfrmainboxb=[2,3,3,2]
yfrmainboxb=[0,0,2,2]
zfrmainboxb=[-5,-5,-5,-5]

xfrmainboxt=[2,3,3,2]
yfrmainboxt=[2,2,2,2]
zfrmainboxt=[-4,-4,-5,-5]

#second blk on top
xsecmainboxf=[1.3,2.7,2.7,1.3]
ysecmainboxf=[3,3,5,5]
zsecmainboxf=[-5.5,-5.5,-5.5,-5.5]

xsecmainboxl=[1.3,1.3,1.3,1.3]
ysecmainboxl=[3,3,5,5]
zsecmainboxl=[-8,-5.5,-5.5,-8]

xsecmainboxr=[2.7,2.7,2.7,2.7]
ysecmainboxr=[3,3,5,5]
zsecmainboxr=[-5.5,-8,-8,-5.5]

xsecmainboxb=[1.3,2.7,2.7,1.3]
ysecmainboxb=[3,3,5,5]
zsecmainboxb=[-8,-8,-8,-8]

xsecmainboxt=[1.3,2.7,2.7,1.3]
ysecmainboxt=[5,5,5,5]
zsecmainboxt=[-5.5,-5.5,-8,-8]

#top most blk 
xtmainboxf=[1.5,2.5,2.5,1.5]
ytmainboxf=[5,5,6,6]
ztmainboxf=[-5.5,-5.5,-5.5,-5.5]

xtmainboxl=[1.5,1.5,1.5,1.5]
ytmainboxl=[5,5,6,6]
ztmainboxl=[-8,-5.5,-5.5,-8]

xtmainboxr=[2.5,2.5,2.5,2.5]
ytmainboxr=[5,5,6,6]
ztmainboxr=[-5.5,-8,-8,-5.5]

xtmainboxb=[1.5,2.5,2.5,1.5]
ytmainboxb=[5,5,6,6]
ztmainboxb=[-8,-8,-8,-8]

xtmainboxt=[1.5,2.5,2.5,1.5]
ytmainboxt=[6,6,6,6]
ztmainboxt=[-5.5,-5.5,-8,-8]

#leftside blk
xlmainboxf=[0.5,1,1,0.5]
ylmainboxf=[0,0,2.5,2.5]
zlmainboxf=[-6,-6,-6,-6]

xlmainboxl=[0.5,0.5,0.5,0.5]
ylmainboxl=[0,0,2.5,2.5]
zlmainboxl=[-8,-6,-6,-8]

xlmainboxr=[1,1,1,1]
ylmainboxr=[0,0,2.5,2.5]
zlmainboxr=[-6,-8,-8,-6]

xlmainboxb=[0.5,1,1,0.5]
ylmainboxb=[0,0,2.5,2.5]
zlmainboxb=[-8,-8,-8,-8]

xlmainboxt=[0.5,1,1,0.5]
ylmainboxt=[2.5,2.5,2.5,2.5]
zlmainboxt=[-6,-6,-8,-8]

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

vflmainboxf=[zip(xflmainboxf,yflmainboxf,zflmainboxf)]
vflmainboxl=[zip(xflmainboxl,yflmainboxl,zflmainboxl)]
vflmainboxr=[zip(xflmainboxr,yflmainboxr,zflmainboxr)]
vflmainboxb=[zip(xflmainboxb,yflmainboxb,zflmainboxb)]
vflmainboxt=[zip(xflmainboxt,yflmainboxt,zflmainboxt)]

vfrmainboxf=[zip(xfrmainboxf,yfrmainboxf,zfrmainboxf)]
vfrmainboxl=[zip(xfrmainboxl,yfrmainboxl,zfrmainboxl)]
vfrmainboxr=[zip(xfrmainboxr,yfrmainboxr,zfrmainboxr)]
vfrmainboxb=[zip(xfrmainboxb,yfrmainboxb,zfrmainboxb)]
vfrmainboxt=[zip(xfrmainboxt,yfrmainboxt,zfrmainboxt)]

vsecmainboxf=[zip(xsecmainboxf,ysecmainboxf,zsecmainboxf)]
vsecmainboxl=[zip(xsecmainboxl,ysecmainboxl,zsecmainboxl)]
vsecmainboxr=[zip(xsecmainboxr,ysecmainboxr,zsecmainboxr)]
vsecmainboxb=[zip(xsecmainboxb,ysecmainboxb,zsecmainboxb)]
vsecmainboxt=[zip(xsecmainboxt,ysecmainboxt,zsecmainboxt)]

vtmainboxf=[zip(xtmainboxf,ytmainboxf,ztmainboxf)]
vtmainboxl=[zip(xtmainboxl,ytmainboxl,ztmainboxl)]
vtmainboxr=[zip(xtmainboxr,ytmainboxr,ztmainboxr)]
vtmainboxb=[zip(xtmainboxb,ytmainboxb,ztmainboxb)]
vtmainboxt=[zip(xtmainboxt,ytmainboxt,ztmainboxt)]

vlmainboxf=[zip(xlmainboxf,ylmainboxf,zlmainboxf)]
vlmainboxl=[zip(xlmainboxl,ylmainboxl,zlmainboxl)]
vlmainboxr=[zip(xlmainboxr,ylmainboxr,zlmainboxr)]
vlmainboxb=[zip(xlmainboxb,ylmainboxb,zlmainboxb)]
vlmainboxt=[zip(xlmainboxt,ylmainboxt,zlmainboxt)]

vertsB1FF = [zip(x01,y01,z01)]
vertsB1LF = [zip(x02,y02,z02)]
vertsB1RF = [zip(x03,y03,z03)]
vertsB1BF = [zip(x04,y04,z04)]
vertsB1RFF = [zip(xRF01,yRF01,zRF01)]
vertsB1RLF = [zip(xRF02,yRF02,zRF02)]
vertsB1RBF = [zip(xRF03,yRF03,zRF03)]
vertsB1RRF = [zip(xRF04,yRF04,zRF04)]
vertsB22FF = [zip(x11,y11,z11)]
vertsB22LF = [zip(x12,y12,z12)]
vertsB22RF = [zip(x13,y13,z13)]
vertsB22BF = [zip(x14,y14,z14)]
vertsB22RFF = [zip(xRF11,yRF11,zRF11)]
vertsB22RLF = [zip(xRF12,yRF12,zRF12)]
vertsB22RBF = [zip(xRF13,yRF13,zRF13)]
vertsB22RRF = [zip(xRF14,yRF14,zRF14)]
vertsB2FF = [zip(x21,y21,z21)]
vertsB2LF = [zip(x22,y22,z22)]
vertsB2RF = [zip(x23,y23,z23)]
vertsB2BF = [zip(x24,y24,z24)]
vertsB2RFF = [zip(xRF21,yRF21,zRF21)]
vertsB2RLF = [zip(xRF22,yRF22,zRF22)]
vertsB2RBF = [zip(xRF23,yRF23,zRF23)]
vertsB2RRF = [zip(xRF24,yRF24,zRF24)]
vertsB3P1FF = [zip(x31,y31,z31)]
vertsB3P1LF = [zip(x32,y32,z32)]
vertsB3P1RF = [zip(x33,y33,z33)]
vertsB3P1BF = [zip(x34,y34,z34)]
vertsB3P1T  = [zip(x35,y35,z35)]
vertsB3P2FF = [zip(x41,y41,z41)]
vertsB3P2LF = [zip(x42,y42,z42)]
vertsB3P2RF = [zip(x43,y43,z43)]
vertsB3P2BF = [zip(x44,y44,z44)]
vertsB3P2T  = [zip(x45,y45,z45)]
vertsB3P3FF = [zip(x51,y51,z51)]
vertsB3P3LF = [zip(x52,y52,z52)]
vertsB3P3RF = [zip(x53,y53,z53)]
vertsB3P3BF = [zip(x54,y54,z54)]
vertsB3P3T  = [zip(x55,y55,z55)]
vertsB4FF = [zip(x61,y61,z61)]
vertsB4LF = [zip(x62,y62,z62)]
vertsB4RF = [zip(x63,y63,z63)]
vertsB4BF = [zip(x64,y64,z64)]
vertsGrass = [zip(x75,y75,z75)]

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

ax.add_collection3d(Poly3DCollection(vflmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vflmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vflmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vflmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vflmainboxt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vfrmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vfrmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vfrmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vfrmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vfrmainboxt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vsecmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vsecmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vsecmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vsecmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vsecmainboxt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vtmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vtmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vtmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vtmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vtmainboxt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vlmainboxf), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vlmainboxl), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vlmainboxr), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vlmainboxb), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vlmainboxt), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB1FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1BF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB1RFF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1RLF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1RRF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB1RBF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB22FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22BF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB22RFF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22RLF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22RRF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB22RBF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB2FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2BF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB2RFF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2RLF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2RRF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB2RBF), zs=0, zdir='x')


ax.add_collection3d(Poly3DCollection(vertsB3P1FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P1LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P1RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P1BF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P1T), zs=0, zdir='x')


ax.add_collection3d(Poly3DCollection(vertsB3P2FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P2LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P2RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P2BF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P2T), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsB3P3FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P3LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P3RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P3BF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB3P3T), zs=0, zdir='x')


ax.add_collection3d(Poly3DCollection(vertsB4FF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB4LF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB4RF), zs=0, zdir='x')
ax.add_collection3d(Poly3DCollection(vertsB4BF), zs=0, zdir='x')

ax.add_collection3d(Poly3DCollection(vertsGrass, facecolors='g'), zs=0, zdir='x')

ax.set_xlabel('X')
ax.set_xlim3d(-10, 10)
ax.set_ylabel('Y')
ax.set_ylim3d(-10, 10)
ax.set_zlabel('Z')
ax.set_zlim3d(-10, 10)
plt.show()