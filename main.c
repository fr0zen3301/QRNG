#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int quantum_superposition() {
    
    // Simulate a 50% probability of collapsins to 0 or 1(polarization)
    // It's being detected vertically or horizontally (0 or 1)
    // Collapse of the wave function
    return rand() % 2; 
}


void save_to_file(int n, const char* filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file\n");
        return;
    }
    printf("Quantum Random Numbers: ");
    // Generate and write the random bits
    for (int i = 0; i < n; i++) {
        int bit = quantum_superposition();
        printf("%d", bit);
        fprintf(file, "%d", bit); // Write the bit (0 or 1)
    }
    printf("\n");
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
    save_to_file(num_bits, random_number);
    return 0;
}
