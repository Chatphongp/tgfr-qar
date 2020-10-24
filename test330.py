import sys
import time
import matplotlib.pyplot as plt
import array
import numpy as np
import pandas as pd
from termcolor import colored

start_time = time.time()

smoothingScale = 4 ## 2 sec per sample

with open('TBA200927-200928.dat', 'rb') as f:
    f.read(0)
    b = f.read()
    f.close()

def RemoveFirstByte_np(arr):
    return np.bitwise_and(arr, 0xFFF)

def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0: 
        val = val - (1 << bits)        
    return val

vTwoComplement = np.vectorize(twos_complement)


def GetValue_np(arr, bitStart, bitLength, coeff, signedBit):
    mask = (2** bitLength) - 1
    arr = np.right_shift(arr, bitStart)
    masked = arr & mask
    if (signedBit):
        return vTwoComplement(masked, signedBit) * coeff
    else:
        return masked * coeff

## read int16 from file buffer
np_data = np.frombuffer(b, dtype=np.int16)

## reshape vector to maxtrix with col = 512 (512 words)
np_data_matrix = np_data.reshape([ -1, 512 ])

print("Frame Size ", np_data_matrix.shape)
## TODO Verify Subframe order and subframe is valid

start_time = time.time()
cas_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 484]), bitStart = 0, bitLength = 12, signedBit=  0, coeff = 0.125)

flaps_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 224]), bitStart = 4, bitLength = 8, signedBit=  0, coeff = 0.25)

masterSW1_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[1::2, 316]), bitStart = 1, bitLength = 1, signedBit=  0, coeff = 1)

masterSW2_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 314]), bitStart = 1, bitLength = 1, signedBit=  0, coeff = 1)

ff1_lsb_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 38]), bitStart = 0, bitLength = 12, signedBit=  0, coeff = 4)
ff1_msb_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 36]), bitStart = 10, bitLength = 2, signedBit=  0, coeff = 4)

ff2_lsb_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 294]), bitStart = 0, bitLength = 12, signedBit=  0, coeff = 4)
ff2_msb_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 292]), bitStart = 10, bitLength = 2, signedBit=  0, coeff = 4)

packcon1_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 58]), bitStart = 0, bitLength = 1, signedBit=  0, coeff = 1)
packcon2_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[1::2, 58]), bitStart = 0, bitLength = 1, signedBit=  0, coeff = 1)


n1eng1_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 22]), bitStart = 0, bitLength = 12, signedBit=  0, coeff = 0.03125)
n1eng2_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 278]), bitStart = 0, bitLength = 12, signedBit=  0, coeff = 0.03125)


nosesw_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 86]), bitStart = 3, bitLength = 1, signedBit=  0, coeff = 1)
lhsw_np = GetValue_np(RemoveFirstByte_np(np_data_matrix[0::2, 86]), bitStart = 1, bitLength = 1, signedBit=  0, coeff = 1)
print("Numpy---\t\t\t %s seconds ---" % (time.time() - start_time))


"""
index = list(item for item in range(50000))
ff1_lsb = ff1_lsb[:50000]
ff1_msb = ff1_msb[:50000] * 2048
ff1 = ff1_lsb + ff1_msb

ff2_lsb = ff2_lsb[:50000]
ff2_msb = ff2_msb[:50000] * 2048
ff2 = ff2_lsb + ff2_msb

nosesw = 1 - nosesw
lhsw = 1 - lhsw

nose_air_min = np.min(np.where(nosesw == 1))
nose_air_max = np.max(np.where(nosesw == 1))

CompareVector(cas, cas_np)
CompareVector(flaps, flaps_np)
CompareVector(n1eng1, n1eng1_np)
CompareVector(ff1_lsb, ff1_lsb_np)

fig, ax = plt.subplots(6)
ax[0].plot(index, flaps, label = "Flaps")

ax[1].plot(index, n1eng1, label = "N1 ENG1")
ax[1].plot(index, n1eng2, label = "N1 ENG2")

ax[2].plot(index, ff1, label = "FF ENG1")
ax[2].plot(index, ff2, label = "FF ENG2")

ax[3].plot(index, masterSW1, label = "MASTER SW1")
ax[3].plot(index, masterSW2, label = "MASTER SW2")

ax[4].plot(index, packcon1, label = "PACK Con 1")
ax[4].plot(index, packcon2, label = "PACK Con 2")


ax[5].plot(index, nosesw, label = "NOSE Squat SW")
ax[5].plot(index, nosesw, label = "LH Squat SW")

for a in ax:
    a.get_xaxis().set_visible(False)
    a.legend()
fig.tight_layout()
"""

##plt.show()



