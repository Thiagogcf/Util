import numpy as np
import cmath


def fourier_transform(x, t):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * np.pi * k * n / N)

    return X


# Example usage
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t)

X = fourier_transform(x, t)

# Print the Fourier transform coefficients
print("Fourier Transform Coefficients:")
for k in range(len(X)):
    print(f"X[{k}] = {X[k]}")