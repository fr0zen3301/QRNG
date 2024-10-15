import qrng_wrapper
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram


n_bits = int(input("Number of bits to generate: "))
filename = "qrn.txt"
qrng_wrapper.seed_rng() # seed the random number generator
qrng_wrapper.generate_qrng_bytes(n_bits, filename)
