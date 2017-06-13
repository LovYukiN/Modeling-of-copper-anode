#! /user/bin/python
#- -coding: UTF-8-*-
from odbAccess import *
odb=openOdb(path='F:\Abaqus Work Content/Verify simple/Job-2.odb')
#指定odb文件的路径
RF=odb.steps['Step-2'].frames[-1].fieldOutputs['RF']
#选择step2的最后一帧输出其RF
center=odb.rootAssembly.nodeSets['TOP']
#将部件中的TOP点集赋值给center变量
centerRF=RF.getSubset(region=center)
#得到center区域的RF值并赋值给变量centerRF
RFValues=centerRF.values
#得到center区域的RF值
cpFile=file('artlcF1.txt','w')
#输出文件定义
for v in RFValues:
    cpFile.write('%10.8F %10.8F %10.8F\n' % (v.data[0], v.data[1], v.data[2]))
cpFile.close()

