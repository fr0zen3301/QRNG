# QRNG
Quantum Random Number Generator(QRNG) used to simulate quantum-based randomness. Unlike classical random number generators, which are algorithmically generated(thus deterministic), the QRNG uses the principles of quantum mechanics to generate truly random numbers. Quantum RNGs leverage phenomena like superposition or photon polarization to produce unpredictable and non-deterministic results.
Through simulation measures a photon(either 0 or 1) and accumulate 8 bits into a byte. 
# #V1.0 - Using software simulations of quantum states.

Since actual hardware is not accessible(currently), the first version simulates quantum states using random functions available in C itself. 

**#V1.0.1 - Added a feauture to save generated random numbers to a file for later use.**

**#V1.0.2 - Combines bits into bytes to generate larger random numbers for encoding data.** 
Randomly measures every bit and accumulates a byte. Provides the result in HEX as output file.

### V2.0 - integrating QRNG with Qiskit to create and manipulate random qubits, simulating the behavior of quantum systems(Actual hardware). In progress...

Kept the QRNG module in C for core functions to maintain performance for the random number generation. The QRNG will be implemented with [Qiskit](https://www.ibm.com/quantum/qiskit), quantum computing framework, and some visualizations of randomness will be added.

Using Qiskit to simulate a quantum channel connection and send a key for AES encryption. QRNG is integrated for generating truly random qubits. 