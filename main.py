import qrng_wrapper

filename = "qrn_txt"
# textfile.encode('UTF-8')
n_bits = 256

qrng_wrapper.quantum_random_bytes(n_bits, filename)
