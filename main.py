import qrng_wrapper
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram


n_bits = int(input("Number of bits to generate: "))
filename = "random_bits.txt"
output_format = input("Enter output format (b for binary, h for hex): ")
qrng_wrapper.seed_rng() # seed the random number generator
qrng_wrapper.generate_qrng_bytes(n_bits, filename, output_format)



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
