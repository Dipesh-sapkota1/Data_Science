# Calculate the normal distrubution of the curve
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mu = 0        # Mean
sigma = 1     # Standard deviation

# Generate x values (range of values on the x-axis)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Compute the normal distribution (PDF) values for each x
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

# Plot the normal distribution curve
plt.plot(x, pdf, label=f'Normal Distribution\nμ={mu}, σ={sigma}')
plt.title('Normal Distribution Curve')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()
