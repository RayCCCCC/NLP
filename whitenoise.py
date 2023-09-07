#!/usr/bin/env python
# coding: utf-8

# In[2]:


import wave
import numpy as np

def add_white_noise(input_file, output_file, noise_amplitude):
    # Open the input WAV file
    with wave.open(input_file, 'rb') as wav_in:
        # Get the audio file parameters
        params = wav_in.getparams()
        num_frames = params.nframes

        # Read the audio data
        audio_data = wav_in.readframes(num_frames)

    # Convert the audio data to a numpy array
    audio_array = np.frombuffer(audio_data, dtype=np.int16)

    # Generate white noise with the same length as the audio
    noise = np.random.normal(scale=noise_amplitude, size=len(audio_array))

    # Add the noise to the audio
    noisy_audio = audio_array + noise

    # Convert the audio back to bytes
    noisy_audio_bytes = noisy_audio.astype(np.int16).tobytes()

    # Write the noisy audio to the output file
    with wave.open(output_file, 'wb') as wav_out:
        wav_out.setparams(params)
        wav_out.writeframes(noisy_audio_bytes)

# Usage example
input_file = 'Ses02F_impro01.wav'
output_file = 'output.wav'
noise_amplitude = 1000  # Adjust the amplitude as desired

add_white_noise(input_file, output_file, noise_amplitude)


# In[ ]:




