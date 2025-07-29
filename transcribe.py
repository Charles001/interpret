from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe_audio(audio_path):
    segments, info = model.transcribe(audio_path, beam_size=5)
    full_text = " ".join([seg.text for seg in segments])
    return full_text.strip(), info.language
