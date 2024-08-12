
"""
'''import numpy as np
import matplotlib.pyplot as plt

def adaptive_noise_cancelation(noisy_signal, clean_signal, filter_length=64, mu=0.01, epsilon=1e-8):
    # Initialize variables
    n = len(noisy_signal)
    noise_estimate = np.zeros(n)
    output_signal = np.zeros(n)
    filter_coefficients = np.zeros((1, filter_length))

    # Apply LMS algorithm for adaptive filtering
    for i in range(n):
        # Calculate the start and end indices for the current segment
        start_idx = max(0, i - filter_length + 1)
        end_idx = i + 1

        # Extract the current segment from noisy and clean signals
        segment_noisy = noisy_signal[start_idx:end_idx][::-1]
        segment_clean = clean_signal[start_idx:end_idx][::-1]

        # Ensure segment_noisy has the correct length
        if len(segment_noisy) < filter_length:
            segment_noisy = np.pad(segment_noisy, (0, filter_length - len(segment_noisy)), mode='constant')

        # Estimate the noise using the adaptive filter
        noise_estimate[i] = np.dot(filter_coefficients, segment_noisy.reshape((filter_length, 1)))[0]

        # Update filter coefficients using LMS algorithm
        error = segment_clean[0] - noise_estimate[i]
        filter_coefficients += mu * error * segment_noisy / (np.dot(segment_noisy, segment_noisy) + epsilon)

        # Apply noise cancellation to the current sample
        output_signal[i] = noisy_signal[i] - noise_estimate[i]

    return output_signal

# Example usage
noisy_signal = np.random.randn(1000)  # Example noisy signal
clean_signal = np.sin(np.linspace(0, 10*np.pi, 1000))  # Example clean signal

filtered_signal = adaptive_noise_cancelation(noisy_signal, clean_signal)

# Plotting the signals
plt.figure(figsize=(10, 6))
plt.plot(noisy_signal, label='Noisy Signal')
plt.plot(clean_signal, label='Clean Signal')
plt.plot(filtered_signal, label='Filtered Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.title('Noise Cancellation Using Adaptive Filter')
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt
import librosa
import sounddevice as sd

# Function to generate delayed Gaussian noise
def generate_delayed_noise(length, std_dev, delay_rate):
    noise = std_dev * np.random.randn(length)
    delayed_noise = np.zeros_like(noise)
    delay_samples = int(delay_rate * len(noise))
    delayed_noise[delay_samples:] = noise[:-delay_samples]  # Apply delay to noise samples
    return delayed_noise

# Function for LMS noise cancellation
def lms_noise_cancellation(primary_input, reference_input, filter_length, delay_rate, learning_rate, num_iterations):
    # Initialize filter coefficients with zeros
    w = np.zeros(filter_length)
    # Number of samples
    N = len(primary_input)
    
    # Initialize output signal
    output_signal = np.zeros(N)
    
    # Iterate through each sample
    for n in range(N):
        # Calculate the delay index based on the delay rate
        delay_index = int(delay_rate * n)
        
        # Extract the delayed input samples for filtering
        x = np.zeros(filter_length)
        for i in range(filter_length):
            if delay_index - i >= 0:
                x[i] = primary_input[delay_index - i]
        
        # Calculate filter output
        y = np.dot(w, x)
      
        # Calculate error
        e = reference_input[n] - y
        
        # Update filter coefficients using LMS algorithm
        w = w + learning_rate * e * x
        
        # Store filtered output
        output_signal[n] = y
    
    return output_signal

# Load the audio file using librosa
audio_file = r"E:\frnds\python\clean_speech\harvard.wav"
audio_signal, sample_rate = librosa.load(audio_file, sr=None)

# Generate delayed Gaussian noise with the same length as the audio signal
noise_std_dev = 0.5
noise_delay_rate = 1 # Adjust delay rate as needed
delayed_noise = generate_delayed_noise(len(audio_signal), noise_std_dev, noise_delay_rate)

# Add delayed noise to the audio signal
noisy_input_signal = audio_signal + delayed_noise

# Parameters for LMS noise cancellation
filter_length = 800
learning_rate = 0.01
num_iterations = 100
delay_rate = 0.5  # Adjust delay rate as needed

# Apply LMS noise cancellation
output_signal = lms_noise_cancellation(noisy_input_signal, audio_signal, filter_length, delay_rate, learning_rate, num_iterations)

# Play original signal, noisy input signal, and filtered output signal using sounddevice (sd)
print("Playing original signal...")
sd.play(audio_signal, sample_rate)
sd.wait()

print("Playing noisy input signal...")
sd.play(noisy_input_signal, sample_rate)
sd.wait()

print("Playing filtered output signal...")
sd.play(output_signal, sample_rate)
sd.wait()

# Plotting (if needed)
time = np.arange(len(audio_signal)) / sample_rate

plt.figure(figsize=(10, 6))
plt.grid(True)

plt.subplot(3, 1, 1)
plt.plot(time, audio_signal, label='Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Audio Signal')

plt.subplot(3, 1, 2)
plt.plot(time, noisy_input_signal, label='Noisy Input Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Noisy Input Signal with Delayed Noise')

plt.subplot(3, 1, 3)
plt.plot(time, output_signal, label='Filtered Output Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Filtered Audio Signal')

plt.tight_layout()
plt.legend()
plt.show()
'''
"""


import numpy as np
import matplotlib.pyplot as plt
import librosa
import sounddevice as sd

# Function to generate delayed Gaussian noise
def generate_delayed_noise(length, std_dev, delay_rate):
    noise = std_dev * np.random.randn(length)
    delayed_noise = np.zeros_like(noise)
    delay_samples = int(delay_rate * len(noise))
    delayed_noise[delay_samples:] = noise[:-delay_samples]  # Apply delay to noise samples
    return delayed_noise

# LMS noise cancellation function
def lms_noise_cancellation(primary_input, reference_input, filter_length, learning_rate, num_iterations):
    # Initialize filter coefficients with zeros
    w = np.zeros(filter_length)
    # Number of samples
    N = len(primary_input)
    
    # Initialize output signal
    output_signal = np.zeros(N)
    
    # Iterate through each sample
    for _ in range(num_iterations):
        for n in range(filter_length, N):
            # Extract the current input samples for filtering
            x = primary_input[n - filter_length:n]
            
            # Calculate filter output
            y = np.dot(w, x)
      
            # Calculate error
            e = reference_input[n] - y
            
            # Update filter coefficients using LMS algorithm
            w = w + learning_rate * e * x
        
        # Store filtered output after each iteration (optional, for visualization)
        output_signal = np.convolve(primary_input, w, mode='same')
    
    return output_signal

# Load the audio file using librosa
audio_file = r"E:\frnds\python\clean_speech\harvard.wav"
audio_signal, sample_rate = librosa.load(audio_file, sr=None)

# Generate delayed Gaussian noise with the same length as the audio signal
noise_std_dev = 0.05
noise_delay_rate = 0.5  # Adjust delay rate as needed
delayed_noise = generate_delayed_noise(len(audio_signal), noise_std_dev, noise_delay_rate)

# Add delayed noise to the audio signal
noisy_input_signal = audio_signal + delayed_noise

# Parameters for LMS noise cancellation
filter_length = 100
learning_rate = 0.001
num_iterations = 100

# Apply LMS noise cancellation
output_signal = lms_noise_cancellation(noisy_input_signal, audio_signal, filter_length, learning_rate, num_iterations)

# Play original signal, noisy input signal, and filtered output signal using sounddevice (sd)
print("Playing original signal...")
sd.play(audio_signal, sample_rate)
sd.wait()

print("Playing noisy input signal...")
sd.play(noisy_input_signal, sample_rate)
sd.wait()

print("Playing filtered output signal...")
sd.play(output_signal, sample_rate)
sd.wait()

# Plotting original signal, noisy input signal, and filtered output signal
time = np.arange(len(audio_signal)) / sample_rate

plt.figure(figsize=(10, 6))
plt.grid(True)

plt.subplot(3, 1, 1)
plt.plot(time, audio_signal, label='Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Audio Signal')

plt.subplot(3, 1, 2)
plt.plot(time, noisy_input_signal, label='Noisy Input Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Noisy Input Signal with Delayed Noise')

plt.subplot(3, 1, 3)
plt.plot(time, output_signal, label='Filtered Output Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Filtered Audio Signal')

plt.tight_layout()
plt.legend()
plt.show()
