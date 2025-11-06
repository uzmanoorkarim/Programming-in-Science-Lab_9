import numpy as np

# Function 1: Read values from a file into an array
# This function reads numerical values from a text file and stores them in a NumPy array.
def read_values_from_file(filename):
    data = np.loadtxt(filename)
    return data
values = read_values_from_file(r"C:\Users\2473732\Downloads\values.txt")
print (values)

# Function 2: Read Oscillatory Wave Data and Compute Statistics
# This function reads a file containing wave data with length and amplitude values into a NumPy array.
# It also computes the mean and maximum amplitude.
def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename, delimiter = ',')
    amplitude = data[:,1]
    mean_amplitude = np.mean(amplitude)
    max_amplitude = np.max(amplitude)
    return mean_amplitude, max_amplitude
             
mean_amp, max_amp = read_oscillatory_wave_data(r"C:\Users\2473732\Downloads\wave_data.csv")
print("Mean amplitude:", mean_amp)
print("Max amplitude:", max_amp)

# Function 3: Read Standing Wave Data and Compute Wave Speed
# This function reads a file containing standing wave data with length and tension values into a NumPy array.
# It also computes the wave speed using v = sqrt(T/μ), where μ = mass per unit length (assumed to be 1 for simplicity).
def read_standing_wave_data(filename):
# Open and read file
    with open(filename) as f:
        lines = f.readlines()[1:]  # skip header
    # Convert data to a NumPy array
    data = np.array([line.strip().split(',') for line in lines], dtype=float)
    # Extract columns
    length = data[:, 0]
    tension = data[:, 1]
    # Given mu = 1  v = sqrt(T/μ) = sqrt(T)
    wave_speed = np.sqrt(tension)
    return length, tension, wave_speed

length, tension, wave_speed = read_standing_wave_data(r"/Users/uzma/Desktop/standing_wave.csv")
print("Each position in the lists corresponds to the same measurement:")
print("Lengths:", length)
print("Tensions:", tension)
print("Wave speeds:", wave_speed)
