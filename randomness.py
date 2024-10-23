import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random numbers
random_numbers = np.random.rand(1000)

# Plot a histogram of the random numbers
plt.figure(figsize=(8, 6))
plt.hist(random_numbers, bins=20, color='purple', edgecolor='black', alpha=0.7)
plt.title("Histogram of Pseudo-Random Numbers")
plt.xlabel("Random Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
