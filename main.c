#include "qrng.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BITS_IN_BYTE 8

void seed_random_generator() {
    srand(time(0));
}

int quantum_superposition() {

    // Simulate a 50% probability of collapsins to 0 or 1(polarization)
    // It's being detected vertically or horizontally (0 or 1(qubits))
    // Collapse of the wave function
    return rand() % 2;
}

void QRNG_bits(int n, const char* filename, const char* format) {
    FILE *file = fopen(filename, "w");
    unsigned char byte = 0; // Accumulate bits into a byte
    int bit_count = 0;
    if (file == NULL) {
        printf("Error opening file\n");
        return;
    }
    // printf("Quantum Random Bits: ");
    // Generate and write the random bits one by one
    for (int i = 0; i < n; i++) {
        int bit = quantum_superposition();

        // check for the format (either b or h
        if (format[0] == 'b') {
            fprintf(file, "%d", bit);
        }
        else if (format[0] == 'h') {
            // Combine the bit into the byte
            byte |= (bit << bit_count);
            bit_count++;

            // Check if there's a byte(8 bits) and reset
            if(bit_count == BITS_IN_BYTE) {
                fprintf(file, "%02X", byte); // Write it into the file
                bit_count = 0; // Reset for the next byte
                byte = 0; // Reset for the next group of bytes
            }
        }
        // printf("%d", bit);
    }
    if (format[0] == 'h' && bit_count > 0) {
        // leftover bits that didn't form a full byte
        fprintf(file, "%02X", byte);
    }
    fprintf(file, "\n");
    fclose(file);
    printf("Random numbers saved to %s in format %c\n", filename, (format[0] == 'h') ? "HEX" : "binary");
}


int main() {
    char* filename = "qr_output.txt";
    char format; // (binary or HEX)
    int num_bits;
    printf("Number of random bits to generate: "); // Ask for the amount of random bits
    scanf("%d", &num_bits);
    printf("Enter output format (b for binary, h for hex): ");
    scanf("%c", &format);
    seed_random_generator(); // seed C's random library to get different results.

    // TO DO: make a seed with user's input

    QRNG_bits(num_bits, filename, &format);
    return 0;
}
