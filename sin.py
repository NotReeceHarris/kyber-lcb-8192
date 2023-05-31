import matplotlib.pyplot as plt
import numpy as np

def smooth_array(arr):

    for i in range(0, 10):

        for idx,x in enumerate(arr):
            arr[idx] = float(arr[idx])


            if idx + 1 != len(arr) and arr[idx] < arr[idx + 1]:
                arr[idx] = arr[idx] + 0.1

            if idx + 1 != len(arr) and arr[idx] > arr[idx + 1]:
                arr[idx] = arr[idx] - 0.1

    return arr

def convertToSin(data):
    encoded_data = []
    for char in data:
        binary = bin(ord(char))[2:].zfill(8)  # Convert character to 8-bit binary string
        waveform = [int(bit) for bit in binary]  # Convert binary string to list of integers
        encoded_data.extend(waveform)  # Append waveform to encoded data
    
    return encoded_data

def convertFromSin(waveform):
    decoded_data = ''
    for i in range(0,len(waveform),8):
        binary = ''.join(str(bit) for bit in waveform[i:i+8])  # Get 8-bit binary string
        char = chr(int(binary,2))  # Convert binary string to character
        decoded_data += char
    
    return decoded_data


data = "Hello World"
encoded = convertToSin(data)
decoded = convertFromSin(encoded)

print('\n---------- ENCODED ----------\n')
print(encoded)

#smoothed = smooth_array(encoded)

""" print('\n---------- SMOOTHED ----------\n')
print(smoothed) """

print('\n---------- DECODED ----------\n')
print(decoded)


print(len)

wave2 = np.cos(np.linspace(0, 2*np.pi, 100))

# Merge the wave arrays element-wise
merged_wave = np.add(encoded, wave2)


plt.plot(smoothed)
plt.xlabel(data)
plt.ylabel('Amplitude')
plt.show()
