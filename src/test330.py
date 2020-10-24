import sys
import time
import matplotlib.pyplot as plt
import array
import numpy as np
import pandas as pd
from termcolor import colored
import seaborn as sns

start_time = time.time()

smoothingScale = 4  ## 2 sec per sample

with open("./data/raw.dat", "rb") as f:
    f.read(0)
    b = f.read()
    f.close()


def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val


def v_twos_complement(val, bits):
    return np.vectorize(twos_complement)


vTwoComplement = np.vectorize(twos_complement)


def GetValue_np(arr, bitStart, bitLength, coeff, signedBit):
    arr = np.bitwise_and(arr, 0xFFF)
    mask = (2 ** bitLength) - 1
    arr = np.right_shift(arr, bitStart)
    masked = np.bitwise_and(arr, mask)
    if signedBit:
        return np.multiply(vTwoComplement(masked, signedBit), coeff)
    else:
        return masked * coeff


def Validate(arr):
    arr = arr[:, 0]
    SYNC_WORD_HEX = [0x247, 0x5B8, 0xA47, 0xDB8]

    for i in range(4):
        syncWord = arr[i::4]

        if (syncWord == SYNC_WORD_HEX[i]).all():
            print(colored("WORD " + str(i) + " PASSED", "green"))
        else:
            print(colored("WORD " + str(i) + " FAILED", "red"))


def get_int16(buffer):
    return np.frombuffer(b, dtype=np.int16)


## read int16 from file buffer
np_data = np.frombuffer(b, dtype=np.int16)


def get_reshape_vector_to_subframe_matix(buffer):
    np_data = get_int16(buffer)
    data = np_data.reshape([-1, 512])
    data = data[:20000, :]
    return data


## reshape vector to maxtrix with col = 512 (512 words)
data = np_data.reshape([-1, 512])
data = data[:20000, :]

print("Frame Size ", data.shape)
## TODO Verify Subframe order and subframe is valid
Validate(data)

start_time = time.time()
cas = GetValue_np(data[0::2, 484], bitStart=0, bitLength=12, signedBit=0, coeff=0.125)

flaps = GetValue_np(data[0::2, 224], bitStart=4, bitLength=8, signedBit=0, coeff=0.25)

masterSW1 = GetValue_np(data[1::2, 316], bitStart=1, bitLength=1, signedBit=0, coeff=1)

masterSW2 = GetValue_np(data[0::2, 314], bitStart=1, bitLength=1, signedBit=0, coeff=1)

ff1 = GetValue_np(data[0::2, 38], bitStart=0, bitLength=12, signedBit=0, coeff=1)
ff2 = GetValue_np(data[0::2, 294], bitStart=0, bitLength=12, signedBit=0, coeff=1)


packcon1 = GetValue_np(data[0::2, 58], bitStart=0, bitLength=1, signedBit=0, coeff=1)
packcon2 = GetValue_np(data[1::2, 58], bitStart=0, bitLength=1, signedBit=0, coeff=1)


n1eng1 = GetValue_np(
    data[0::2, 22], bitStart=0, bitLength=12, signedBit=0, coeff=0.03125
)
n1eng2 = GetValue_np(
    data[0::2, 278], bitStart=0, bitLength=12, signedBit=0, coeff=0.03125
)


nosesw = GetValue_np(data[0::2, 86], bitStart=3, bitLength=1, signedBit=0, coeff=1)
lhsw = GetValue_np(data[0::2, 86], bitStart=1, bitLength=1, signedBit=0, coeff=1)
print("Numpy---\t\t\t %s seconds ---" % (time.time() - start_time))

index = list(item for item in range(len(ff1)))
"""

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
sns.set()
plt.plot(index, flaps, label="flaps")
plt.plot(index, n1eng1, label="n1eng1")
plt.plot(index, n1eng2, label="n1eng2")
plt.legend()
plt.tight_layout()
plt.show()
