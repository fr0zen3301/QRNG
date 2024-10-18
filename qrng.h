#ifndef QRNG_H
#define QRNG_H

void QRNG_bits(int n, const char* filename, const char* format);
int quantum_superposition();
void seed_random_generator();

#endif // QRNG_H