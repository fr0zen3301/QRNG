import qrng_wrapper

n_bits = int(input("Number of bits to generate: "))
filename = "qrn.txt"
qrng_wrapper.seed_rng() # seed the random number generator
qrng_wrapper.generate_qrng_bytes(n_bits, filename)
