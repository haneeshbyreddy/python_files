import numpy as np
'''
def RLS_Alogirthm(input_signal,derised_signal,order,lambda1):
      #size of a input_signal
    lenght=len(input_signal)
    h=np.zeros(lenght) #size of a weight vector 
    p=(1/lambda1)*np.eye(lenght) #p vecor
    for i in range(lenght):
        signal=np.dot(input_signal.transpose(),h)
        error_factor=derised_signal-signal
        k=np.dot(p,input_signal)/lambda1+np.dot(np.dot(np.transpose(input_signal),p),input_signal)
        h=h+np.dot(k,error_factor)
        p=1/lambda1(p-np.dot(np.dot(k,np.transpose(input_signal)),p))
    return h
'''
import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt

def RLS_Alogirthm(input_signal, desired_signal, order, lambda1):
    length = len(input_signal)
   
    h = np.zeros((length, 1))
    p = np.eye(length) * 1e3  # Initialize the inverse correlation matrix
    y = np.zeros((length, 1)) 
    for i in range(length):  # Adjusted loop bounds to stay within array bounds
        signal = np.dot(input_signal,h)
        error_factor = desired_signal - signal
        # Assuming k is a scalar and error_factor is a column vector (n x 1)
        k = np.dot(p, input_signal) / lambda1 + np.dot(np.dot(np.transpose(input_signal), p), input_signal)
        error_factor = error_factor.reshape((-1, 1))  # Ensure error_factor is a column vector if not already

        # Option 1: Broadcasting k to match error_factor
        h = h + k * error_factor 
        
        # Option 2: Dot product with appropriate transposition
        #h = h + np.dot(k.reshape(1, -1), error_factor.reshape(-1)).reshape(-1)

        p = 1 / lambda1 * (p - np.dot(np.dot(k, np.transpose(input_signal)), p))
        y = np.dot(h, input_signal)
    return y

order = 50  # Filter order
forgetting_factor = 0.99  # Forgetting factor
file_path = r"E:\frnds\python\clean_speech\harvard.wav"
audio_signal, sample_rate = librosa.load(file_path, sr=None)
noise = 0.05 * np.random.randn(len(audio_signal))
noisy_input_signal = audio_signal + noise

output_signal = RLS_Alogirthm(audio_signal[:10000], noisy_input_signal[:10000], order, forgetting_factor)
sf.write("output1.wav", output_signal, sample_rate)
sf.write("noise_signal.wav", noisy_input_signal, sample_rate)

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(audio_signal)
plt.title('Original Signal')

plt.subplot(3, 1, 2)
plt.plot(noise)
plt.title('Noise Signal')

plt.subplot(3, 1, 3)
plt.plot(output_signal)
plt.title('Filtered Signal (RLS)')

plt.tight_layout()
plt.show()
