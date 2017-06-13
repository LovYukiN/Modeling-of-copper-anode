#! /user/bin/python
#- -coding: UTF-8-*-
from odbAccess import *
odb=openOdb(path='F:\Abaqus Work Content/Verify simple/Job-2.odb')
#ָ��odb�ļ���·��
RF=odb.steps['Step-2'].frames[-1].fieldOutputs['RF']
#ѡ��step2�����һ֡�����RF
center=odb.rootAssembly.nodeSets['TOP']
#�������е�TOP�㼯��ֵ��center����
centerRF=RF.getSubset(region=center)
#�õ�center�����RFֵ����ֵ������centerRF
RFValues=centerRF.values
#�õ�center�����RFֵ
cpFile=file('artlcF1.txt','w')
#����ļ�����
for v in RFValues:
    cpFile.write('%10.8F %10.8F %10.8F\n' % (v.data[0], v.data[1], v.data[2]))
cpFile.close()

