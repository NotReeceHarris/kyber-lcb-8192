from secrets import token_hex
from textwrap import wrap

import hashlib

import numpy as np
import random
import matplotlib.pyplot as plt

def generate_sine_wave(seed, duration=2, frequency=1, sampling_rate=4096):
    random.seed(hashlib.md5(seed.encode()).hexdigest())
    num_samples = int(duration * sampling_rate)
    phase_offset = random.uniform(0, 2 * np.pi)
    t = np.linspace(0, duration, num_samples)
    waveform = np.sin(2 * np.pi * frequency * t + phase_offset)
    return waveform

def keyGeneration():
    key = token_hex(4096)
    key_with_newlines = '\n'.join(wrap(key, 64))
    return '----------------- START LCB-8192 UNIVERSAL KEY -----------------\n' + key_with_newlines + '\n------------------ END LCB-8192 UNIVERSAL KEY ------------------'

def removeArmor(key):
    # Remove the armor header and footer
    key = key.replace('----------------- START LCB-8192 UNIVERSAL KEY -----------------\n', '')
    key = key.replace('\n------------------ END LCB-8192 UNIVERSAL KEY ------------------', '')

    # Remove the newlines within the key
    key = key.replace('\n', '')

    return key


def convertToSin(data):
    pass

def encrypt(key):

    for idx, x in enumerate(wrap(key, 64)):
        sin = generate_sine_wave(x)
        print(sin)

        plt.plot(sin)
        plt.xlabel(idx)
        plt.ylabel('Amplitude')

    plt.title(hashlib.md5(key.encode()).hexdigest())
    plt.show()