# QRNG
Quantum Random Number Generator(QRNG) used to simulate quantum-based randomness. Unlike classical random number generators, which are algorithmically generated(thus deterministic), the QRNG uses the principles of quantum mechanics to generate truly random numbers. Quantum RNGs leverage phenomena like superposition or photon polarization to produce unpredictable and non-deterministic results.

# #V1.0 - Using software simulations of quantum states.

Since actual hardware is not accessible(currently), the first version simulates quantum states using random functions available in C itself. 

**#V1.0.1 - Added a feauture to save generated random numbers to a file for later use.**

**#V1.0.2 - Combines bits into bytes to generate larger random numbers for encoding data.** 
Randomly measures every bit and accumulates a byte. Provides the result in HEX as output file.

Upcome in future versions - V1.1 contains a simplified test for Bell's inequality violation, which shows that the QRNG mimics actual quantum randomness, not classical one.