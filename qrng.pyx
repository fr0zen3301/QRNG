cdef extern from "qrng.h":
    int quantum_superposition()
    void QRNG_bits(int n, const char* filename, const char* format)
    void seed_random_generator()

# define python function to wrap QRNG_bytes
def generate_qrng_bytes(int num_bits, str filename, str format):
    cdef bytes c_filename_bytes = filename.encode('utf-8')
    cdef bytes c_format = format.encode('utf-8')

    cdef const char* c_filename = c_filename_bytes # convert Python string to C str
    QRNG_bits(num_bits, c_filename, c_format)

def get_quantum_bit():
    return quantum_superposition()

def seed_rng():
    seed_random_generator()