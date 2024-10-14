cdef extern from "qrng.h":
    int quantum_superposition()
    void QRNG_bytes(int n, const char* filename)
    void seed_random_generator()

# define python function to wrap QRNG_bytes
def generate_qrng_bytes(int num_bits, str filename):
    cdef bytes c_filename_bytes = filename.encode('utf-8')

    cdef const char* c_filename = c_filename_bytes # convert Python string to C str
    QRNG_bytes(num_bits, c_filename)

def get_quantum_bit():
    return quantum_superposition()

def seed_rng():
    seed_random_generator()