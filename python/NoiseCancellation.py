import numpy as np
import matplotlib.pyplot as plt

#desired signal + noise
np.random.seed(0)
t = np.linspace(0, 1, 10000)
desired_signal = np.sin(2 * np.pi * 5 * t)  
noise = 0.5 * np.random.randn(len(t))  
observed_signal = desired_signal + noise

# LMS algorithm 
def lms_noise_cancellation(observed_signal, filter_length=20, learning_rate=0.01, no_of_iterations=100):
    w = np.zeros(filter_length)  
    estimated_signal = np.zeros_like(observed_signal)  
    error = np.zeros_like(observed_signal) 

    for _ in range(no_of_iterations):
        for n in range(filter_length, len(observed_signal)):
            x = observed_signal[n-filter_length:n]  # Input vector (past observations)
            estimated_desired = np.dot(w, x)  # Estimate desired signal
            error[n] = observed_signal[n] - estimated_desired  # Calculate error
            w = w + learning_rate * error[n] * x  # Update filter coefficients

    # Apply the estimated filter to cancel noise
    for n in range(filter_length, len(observed_signal)):
        x = observed_signal[n-filter_length:n]
        estimated_signal[n] = np.dot(w, x) # updated y(n)

    return estimated_signal, error

# Apply LMS noise cancellation
estimated_signal, error = lms_noise_cancellation(observed_signal)

# Plot results
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, desired_signal, label='Desired Signal')
plt.title('Before Noise Cancellation')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, observed_signal, label='Observed Signal')
plt.title('With Added Noise')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, estimated_signal, label='Estimated Signal')
plt.title('After Noise Cancellation')
plt.legend()

plt.tight_layout()
plt.show()
