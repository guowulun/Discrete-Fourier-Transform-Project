import cmath
import math

def fft(x):
    """
    Compute the Fast Fourier Transform (FFT) of a sequence x using the Cooley-Tukey algorithm.
    Assumes len(x) is a power of 2.
    """
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Example usage
if __name__ == "__main__":
    # Example signal: a simple sine wave
    import math
    N = 8  # Must be power of 2
    signal = [math.sin(2 * math.pi * 4 * i / N) for i in range(N)]  # 4 Hz sine wave
    print("Original signal:", signal)
    result = fft(signal)
    print("FFT result:", result)
