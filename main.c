#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int quantum_superposition() {
    
    // Simulate a 50% probability of collapsins to 0 or 1(polarization)
    
    // Collapse of the wave function
    return rand() % 2; 
}

void quantum_random_numbers(int n) {
    printf("Quantum Random Numbers: ");
    for (int i = 0; i < n; i++) {
        printf("%d", quantum_superposition());
    }
    printf("\n");
}

int main() {
    int num_bits; // Ask for the amount of random bits
    printf("Number of random bits to generate: ");
    scanf("%d", &num_bits); 
    srand(time(0));
    quantum_random_numbers(num_bits);
    return 0;
}
