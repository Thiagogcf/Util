# Importing necessary modules
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# Downloading and loading all models
preload_models()

# Poem prompt
text_prompt = """
    In the quiet of the evening, under the star's soft glow,
    The world feels soft and peaceful, as the gentle breezes blow.
    The moonlight casts long shadows, as it dances on the sea,
    And in this moment of tranquility, my heart is truly free.
    [laughs]
"""

# Generating audio from the text
audio_array = generate_audio(text_prompt)

# Saving the generated audio to disk
write_wav("poem_generation.wav", SAMPLE_RATE, audio_array)

# Playing the text in the notebook (if applicable)
Audio(audio_array, rate=SAMPLE_RATE)


#pip install git+https://github.com/suno-ai/bark.git
