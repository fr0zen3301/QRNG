#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BITS_IN_BYTE 8

int quantum_superposition() {
    
    // Simulate a 50% probability of collapsins to 0 or 1(polarization)
    // It's being detected vertically or horizontally (0 or 1)
    // Collapse of the wave function
    return rand() % 2; 
}


void QRNG_bytes(int n, const char* filename) {
    FILE *file = fopen(filename, "w");
    unsigned char byte = 0; // Accumulate bits into a byte
    int bit_count = 0;
    if (file == NULL) {
        printf("Error opening file\n");
        return;
    }
    printf("Quantum Random Bits: ");
    // Generate and write the random bits
    for (int i = 0; i < n; i++) {
        int bit = quantum_superposition();
        // printf("%d", bit);
        
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
    fprintf(file, "\n");
    printf("\n");
    // Leftovers bits that didn't form a full byte
    if (bit_count > 0) {
        printf(" ---> Partial Byte: %02X\n", byte);
    }
    // Close the file
    fclose(file);
    printf("Random numbers saved to %s\n", filename);
}

int main() {
    char* random_number = "quantum_random_number.txt";
    int num_bits; // Ask for the amount of random bits
    printf("Number of random bits to generate: ");
    scanf("%d", &num_bits);
    srand(time(0)); // To not get the same sequence every time
    QRNG_bytes(num_bits, random_number);
    return 0;
}
