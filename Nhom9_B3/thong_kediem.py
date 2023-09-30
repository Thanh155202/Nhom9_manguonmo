import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])
print(in_data)
print('Tong so sinh vien tham gia mon hoc :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
tongdiemA= in_data[:,3]
print('Tong sinh vien dat diem A:')
print(np.sum(tongdiemA))
tongdiemBc= in_data[:,4]
print('Tong sinh vien dat diem B+:')
print(np.sum(tongdiemBc))
tongdiemB= in_data[:,5]
print('Tong sinh vien dat diem B:')
print(np.sum(tongdiemB))
tongdiemCc= in_data[:,6]
print('Tong sinh vien dat diem C+:')
print(np.sum(tongdiemCc))
tongdiemC= in_data[:,7]
print('Tong sinh vien dat diem C:')
print(np.sum(tongdiemC))
tongdiemDc= in_data[:,8]
print('Tong sinh vien dat diem D+:')
print(np.sum(tongdiemDc))
tongdiemD= in_data[:,9]
print('Tong sinh vien dat diem D:')
print(np.sum(tongdiemD))
tongdiemF= in_data[:,10]
print('Tong sinh vien dat diem F:')
print(np.sum(tongdiemF))
maxx = 0
minn = 9999999
for i in range (0, 9):
    sum1 = 0
    for j in range (3, 10):
        sum1 += np.sum(in_data[i,j])
    if (sum1 >= maxx):
        maxx = sum1
        lopp = in_data[i,0]
    if (sum1 <= minn):
        minn = sum1
        lopmin = in_data[i,0]
    print ("Lop ", in_data[i, 0], " ", sum1)
print("Lop ", lopp, "co nhieu sinh vien duoc diem >= D nhieu nhat voi ", maxx, " sinh vien")
print("Lop ", lopmin, "co it sinh vien duoc diem >= D nhieu nhat voi ", minn, " sinh vien")
diemL1 = np.sum(in_data[:, 11])
diemL2 = np.sum(in_data[:, 12])
if (diemL1 > diemL2):
    print ("co nhieu sinh vien qua L1 hon L2")
elif (diemL1 < diemL2):
    print("co nhieu sinh vien qua L2 hon L1")
else:
    print("So sinh vien qua L1 va L2 la nhu nhau")

diemA = in_data[:,3]
diemBc = in_data[:,4]
diemB = in_data[:,5]
diemCc = in_data[:,6]
diemC = in_data[:,7]
diemDc = in_data[:,8]
diemD = in_data[:,9]
diemF = in_data[:,10]
print('Tong sv:',tongsv)
maxa = diemA.max()
i, = np.where(diemA == maxa)
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
maxBc = diemBc.max()
i, = np.where(diemBc == maxBc)
print('lop co nhieu diem B+ la {0} co {1} sv dat diem B+'.format(in_data[i,0],maxBc))
maxB = diemB.max()
i, = np.where(diemBc == maxBc)
print('lop co nhieu diem B la {0} co {1} sv dat diem B'.format(in_data[i,0],maxB))
maxCc = diemBc.max()
i, = np.where(diemCc == maxCc)
print('lop co nhieu diem C+ la {0} co {1} sv dat diem C+'.format(in_data[i,0],maxCc))
maxC = diemC.max()
i, = np.where(diemC == maxC)
print('lop co nhieu diem C la {0} co {1} sv dat diem C'.format(in_data[i,0],maxC))
maxDc = diemDc.max()
i, = np.where(diemDc == maxDc)
print('lop co nhieu diem D+ la {0} co {1} sv dat diem D+'.format(in_data[i,0],maxDc))
maxD = diemD.max()
i, = np.where(diemD == maxD)
print('lop co nhieu diem D la {0} co {1} sv dat diem D'.format(in_data[i,0],maxD))
maxF = diemF.max()
i, = np.where(diemF == maxF)
print('lop co nhieu diem F la {0} co {1} sv diem F'.format(in_data[i,0],maxF))

plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
plt.plot(range(len(diemB)),diemB,'b-',label="Diem B")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
plt.plot(range(len(diemCc)),diemCc,'p-',label="Diem C +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
plt.plot(range(len(diemC)),diemC,'y-',label="Diem C")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()

plt.plot(range(len(diemDc)),diemDc,'o-',label="Diem D +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()

plt.plot(range(len(diemD)),diemD,'r-',label="Diem D")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
plt.plot(range(len(diemF)),diemF,'g-',label="Diem F")

plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()
