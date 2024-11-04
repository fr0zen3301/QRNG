import qrng_wrapper
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram
from cryptography.hazmat.primitives.ciphers import  Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

n_bits = int(input("Number of bits to generate: "))
filename = "random_bits.txt"
output_format = input("Enter output format (b for binary, h for hex): ")
qrng_wrapper.seed_rng() # seed the random number generator
qrng_wrapper.generate_qrng_bytes(n_bits, filename, output_format)


def get_AESkey_from_qrng(qrng_output):
    with open(qrng_output, 'r') as file:
        qrng_bits = file.read().strip()

    # extract the first 256 bits (32 bytes) for AES-256
    aes_key = qrng_bits[:256]

    # convert the binary string to bytes
    aes_key_bytes = int(aes_key, 2).to_bytes(32, 'big') # 32 bytes for 256 bits
    return aes_key_bytes


def aes_encrypt(plaintext, key):
    """
   Generate a random IV ( Initialization Vector), block of random or pseudo-random data used as
   an input to the first block of encryption in block cipher modes. It used to be ensure that the same
   plaintext will encrypt to different ciphertexts even when the same key is used, provides semantic security.
    """
    iv = os.urandom(16)
    backend = default_backend()
    # create AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend)
    encyptor = cipher.encryptor()

    # padding plaintext to be a multiple of block size (AES block size is 16 bytes)
    padding_length = 16 - (len(plaintext)%16)
    padded_plaintext = plaintext + (chr(padding_length) * padding_length).encode()

    ciphertext = encyptor.update(padded_plaintext) + encyptor.finalize()

    return iv, ciphertext

aes_key = get_AESkey_from_qrng("random_bits.txt")
plaintext = b"this is a plaintext"
iv, ciphertext = aes_encrypt(plaintext, aes_key)

# print("IV:", iv.hex())
print("AES Key:", ciphertext.hex())

# FOR FUTURE DEVELOPMENT
# from qiskit import QuantumCircuit
# import matplotlib.pyplot as plt
#
# #import matplotlib to draw
#
# # Create a circuit with a register of three qubits
# circ = QuantumCircuit(5)
# # H gate on qubit 0, putting this qubit in a superposition of |0> + |1>.
# circ.h(0)
# # A CX (CNOT) gate on control qubit 0 and target qubit 1 generating a Bell state.
# circ.cx(0, 1)
# # CX (CNOT) gate on control qubit 0 and target qubit 2 resulting in a GHZ state.
# circ.cx(0, 2)
# circ.s(3)
# circ.cx(1, 4)
# # Draw the circuit
# circ.draw(output='mpl')
# plt.show() # show
