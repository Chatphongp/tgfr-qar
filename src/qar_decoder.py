import numpy as np
from termcolor import colored


def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
    return val


def v_twos_complement(val, bits):
    return np.vectorize(twos_complement)


def get_value_np(arr, bitStart, bitLength, coeff, signedBit):
    arr = np.bitwise_and(arr, 0xFFF)
    mask = (2 ** bitLength) - 1
    arr = np.right_shift(arr, bitStart)
    masked = np.bitwise_and(arr, mask)
    if signedBit:
        return np.multiply(v_twos_complement(masked, signedBit), coeff)
    else:
        return masked * coeff


def validate(arr):
    arr = arr[:, 0]
    SYNC_WORD_HEX = [0x247, 0x5B8, 0xA47, 0xDB8]

    for i in range(4):
        syncWord = arr[i::4]

        if (syncWord == SYNC_WORD_HEX[i]).all():
            print(colored("WORD " + str(i) + " PASSED", "green"))
        else:
            print(colored("WORD " + str(i) + " FAILED", "red"))


def get_int16(buffer):
    return np.frombuffer(buffer, dtype=np.int16)


def get_reshape_vector_to_subframe_matix(buffer):
    np_data = get_int16(buffer)
    data = np_data.reshape([-1, 512])
    data = data[:20000, :]
    return data
