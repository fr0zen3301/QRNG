cdef extern from "qrng.h":
    int quantum_superposition()
    void QRNG_bytes(int n, const char* filename)

def quantum_superposition_C():
    return quantum_superposition()

def quantum_random_bytes(int n, str filename):
    QRNG_bytes(n, filename.encode('utf-8'))