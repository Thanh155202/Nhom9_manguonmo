import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print('Danh sách sinh viên đi thi')
print(in_data)

soSV= in_data[:,1]
diemAc = in_data[:,2]
diemA = in_data[:,3]
diemBc = in_data[:,4]
diemB = in_data[:,5]
diemCc = in_data[:,6]
diemC = in_data[:,7]
diemDc = in_data[:,8]
diemD = in_data[:,9]
diemF = in_data[:,10]
diemL1 = in_data[:,11]
diemL2 = in_data[:,12]
diemTX1 = in_data[:,13]
diemTX2 = in_data[:,14]
diemCK = in_data[:,15]

print('Tổng số sinh viên đi thi: {0}'.format(np.sum(soSV)))
print('Tổng số sinh viên thi đạt: {0}'.format(np.sum(soSV)-np.sum(diemF)))
print('Tổng số sinh viên thi trượt: {0}'.format(np.sum(diemF)))

maxAc = diemAc.max()
iac, = np.where(diemAc == maxAc)
print('Lớp có nhiều điểm A+ là {0} có {1} SV đạt điểm A+'.format(in_data[iac,0],maxAc))
maxA = diemA.max()
ia, = np.where(diemA == maxA)
print('Lớp có nhiều điểm A là {0} có {1} SV đạt điểm A'.format(in_data[ia,0],maxA))
maxBc = diemBc.max()
ibc, = np.where(diemBc == maxBc)
print('Lớp có nhiều điểm B+ là {0} có {1} SV đạt điểm B+'.format(in_data[ibc,0],maxBc))
maxB = diemB.max()
ib, = np.where(diemB == maxB)
print('Lớp có nhiều điểm B là {0} có {1} SV đạt điểm B'.format(in_data[ib,0],maxB))
maxCc = diemCc.max()
icc, = np.where(diemCc == maxCc)
print('Lớp có nhiều điểm C+ là {0} có {1} SV đạt điểm C+'.format(in_data[icc,0],maxCc))
maxC = diemC.max()
ic, = np.where(diemC == maxC)
print('Lớp có nhiều điểm C là {0} có {1} SV đạt điểm C'.format(in_data[ic,0],maxC))
maxDc = diemDc.max()
idc, = np.where(diemDc == maxDc)
print('Lớp có nhiều điểm D+ là {0} có {1} SV đạt điểm D+'.format(in_data[idc,0],maxDc))
maxD = diemD.max()
id1, = np.where(diemD == maxD)
print('Lớp có nhiều điểm D là {0} có {1} SV đạt điểm D'.format(in_data[id1,0],maxD))
maxF = diemF.max()
if1, = np.where(diemF == maxF)
print('Lớp có nhiều điểm F là {0} có {1} SV đạt điểm F'.format(in_data[if1,0],maxF))

_diem = ['A+','A','B+','B','C+','C','D+','D','F']

plt.figure('Lớp 1')
plt.plot(_diem,in_data[0,2:11],'b-')
plt.xlabel('Điểm')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.show()

plt.figure('Lớp 2')
plt.plot(_diem,in_data[1,2:11],'b-')
plt.xlabel('Điểm')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.show()

plt.figure('Lớp 3')
plt.plot(_diem,in_data[2,2:11],'b-')
plt.xlabel('Điểm')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.show()


