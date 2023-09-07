

from pydub import AudioSegment
import numpy as np

# 加载目标音频文件和噪声音频文件
target_audio = AudioSegment.from_file("target_audio.wav", format="wav")
noise_audio_1 = AudioSegment.from_file("Hard Rain Strong Winds.wav", format="wav")
noise_audio_1 = noise_audio_1 - 10
# 重复噪声音频以匹配目标音频的长度
while len(noise_audio_1) < len(target_audio):
    noise_audio_1 += noise_audio_1

# 裁剪噪声音频以匹配目标音频的长度
noise_audio_1 = noise_audio_1[:len(target_audio)]

# 将噪声音频与目标音频叠加
result_audio_1 = target_audio.overlay(noise_audio_1)

# 保存合并后的音频文件
result_audio_1.export("result_audio1.wav", format="wav")
