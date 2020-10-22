import sys
import time
import matplotlib.pyplot as plt
import array
import numpy as np
import pandas as pd
import math

start_time = time.time()

with open('raw.dat', 'rb') as f:
    f.read(4096)
    b = f.read()
    f.close()

def RemoveFirstByte(val):
    return val & 0xFFF

def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0: 
        val = val - (1 << bits)        
    return val

def GetValue (raw, bitStart, bitLength, coeff, signedBit):
    mask = (2 ** bitLength) - 1 ## eg. bitLength 11 = 0b11111111111 = 2047
    raw = raw >> bitStart
    masked = raw & mask

    if (signedBit):
        return twos_complement(masked, 12) * coeff
    else:
        return masked * coeff


## Vectorize Function
vRemoveFirstByte = np.vectorize(RemoveFirstByte)
vGetValue = np.vectorize(GetValue)


## read int16 from file buffer
np_data = np.frombuffer(b, dtype=np.int16)

## reshape vector to maxtrix with col = 512 (512 words)
np_data_matrix = np_data.reshape([ -1, 512 ])

## Ground Speed Word 1, bitLength = 12 , coeff = 0.25
gs = vGetValue(vRemoveFirstByte(np_data_matrix[:, 1]) ,bitStart = 0, bitLength =  12, signedBit=  0, coeff = 0.25 )

## Altitude Word 123, bitLength = 12 (included sign) , coeff  = 32; use 0.32 to scale down
alt = vGetValue(vRemoveFirstByte(np_data_matrix[:, 123]), bitStart = 0, bitLength = 12, signedBit=  12, coeff = 0.32)


index = list(item for item in range(len(gs)))
plt.plot(index, gs, label = "GS (kts)")
plt.plot(index, alt, label="ALT (FL)")
plt.legend()
plt.show()


print("--- %s seconds ---" % (time.time() - start_time))