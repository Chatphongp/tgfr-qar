import time
import sys
import os
import http.server
import socketserver
import seaborn as sns
import matplotlib.pyplot as plt
import qar_decoder as qd
import settings


def main(raw_filename: str):

    with open(raw_filename, "rb") as f:
        f.read(0)
        b = f.read()
        f.close()
    data = qd.get_reshape_vector_to_subframe_matrix(b)

    print("Frame Size ", data.shape)

    qd.validate(data)

    start_time = time.time()

    cas = qd.get_value_np(
        data[0::2, 484], bitStart=0, bitLength=12, signedBit=0, coeff=0.125
    )

    flaps = qd.get_value_np(
        data[0::2, 224], bitStart=4, bitLength=8, signedBit=0, coeff=0.25
    )

    masterSW1 = qd.get_value_np(
        data[1::2, 316], bitStart=1, bitLength=1, signedBit=0, coeff=1
    )

    masterSW2 = qd.get_value_np(
        data[0::2, 314], bitStart=1, bitLength=1, signedBit=0, coeff=1
    )

    ff1 = qd.get_value_np(
        data[0::2, 38], bitStart=0, bitLength=12, signedBit=0, coeff=1
    )
    ff2 = qd.get_value_np(
        data[0::2, 294], bitStart=0, bitLength=12, signedBit=0, coeff=1
    )

    packcon1 = qd.get_value_np(
        data[0::2, 58], bitStart=0, bitLength=1, signedBit=0, coeff=1
    )
    packcon2 = qd.get_value_np(
        data[1::2, 58], bitStart=0, bitLength=1, signedBit=0, coeff=1
    )

    n1eng1 = qd.get_value_np(
        data[0::2, 22], bitStart=0, bitLength=12, signedBit=0, coeff=0.03125
    )
    n1eng2 = qd.get_value_np(
        data[0::2, 278], bitStart=0, bitLength=12, signedBit=0, coeff=0.03125
    )

    nosesw = qd.get_value_np(
        data[0::2, 86], bitStart=3, bitLength=1, signedBit=0, coeff=1
    )
    lhsw = qd.get_value_np(
        data[0::2, 86], bitStart=1, bitLength=1, signedBit=0, coeff=1
    )
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


PORT = 9000


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        if path == "/777":
            os.system("ls -l")
        elif path == "/330":
            os.system("ls -la")
        else:
            if len(sys.argv) == 1:
                filename = "./data/raw.dat"
            else:
                filename = sys.argv[1]
            # filename = "./data/raw.dat"
            main(filename)


if __name__ == "__main__":

    PORT = settings.QR_DECODER_PORT
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()