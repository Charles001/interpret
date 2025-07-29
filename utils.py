import tempfile
from pydub import AudioSegment
import os

def convert_audio_to_wav(uploaded_file):
    # suffix = ".mp3" if uploaded_file.name.endswith(".mp3") else ".wav"
    if uploaded_file.name.endswith(".mp3"):
        suffix = ".mp3"
    elif uploaded_file.name.endswith(".m4a"):
        suffix = ".m4a"
    else:
        suffix = ".wav"
    audio_temp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    audio_temp.write(uploaded_file.read())
    audio_temp.close()

    if suffix == ".wav":
        return audio_temp.name

    if suffix == ".mp3":
        sound = AudioSegment.from_mp3(audio_temp.name)
        wav_temp_path = audio_temp.name.replace(".mp3", ".wav")
    else:
        sound = AudioSegment.from_file(audio_temp.name, format='m4a')
        wav_temp_path = audio_temp.name.replace(".m4a", ".wav")
    sound.export(wav_temp_path, format="wav")
    return wav_temp_path

def save_audio_temp(filename):
    path = os.path.join("outputs", filename)
    os.makedirs("outputs", exist_ok=True)
    return path
