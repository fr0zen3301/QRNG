cdef extern from "qrng.h":
    void QRNG_bytes(int n, const char* filename)

def quantum_random_bytes(int n, str filename):
    QRNG_bytes(n, filename.encode('utf-8')) # encode to not get TypeError