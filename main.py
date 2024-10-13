import qrng_wrapper

filename = "qrn.txt"
# number of bits
n_bits = 260

qrng_wrapper.quantum_random_bytes(n_bits, filename)
