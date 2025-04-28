import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Generate mock gravitational wave data (replace with real data later)
np.random.seed(42)
time = np.linspace(0, 10, 1000)  # Time array from 0 to 10 seconds
signal = np.sin(2 * np.pi * 50 * time)  # Example wave signal with frequency of 50 Hz
noise = np.random.normal(0, 0.5, signal.shape)  # Add some noise
data = signal + noise  # Mock data: signal + noise

# Function for Butterworth low-pass filtering
def butter_lowpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs  # Nyquist frequency
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_data = lfilter(b, a, data)
    return filtered_data

# Filter parameters
sampling_rate = 1000  # 1000 Hz
cutoff_frequency = 60  # 60 Hz cutoff frequency

# Apply the filter
filtered_signal = butter_lowpass_filter(data, cutoff_frequency, sampling_rate)

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(time, data, label="Noisy Signal", color="orange")
plt.title("Raw Gravitational Wave Data (Mock)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, filtered_signal, label="Filtered Signal", color="blue")
plt.title("Filtered Gravitational Wave Data")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
