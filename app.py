import streamlit as st
from transcribe import transcribe_audio
from translate import translate_text
# from synthesise import synthesise_speech
from utils import convert_audio_to_wav, save_audio_temp
import os

st.set_page_config(page_title="Interpret Demo", layout="centered")

st.image("assets/pytools_logo_02.png", width=160)

st.title("Interpret (phase 1)")
st.markdown("Bidirectional speech ↔ text ↔ speech demo")

mode = st.radio("Select Mode", ["Hausa → English", "English → Hausa", "French → English", "English → French", "Afrikaans → English", "English → Afrikaans"])

uploaded_file = st.file_uploader("Upload an audio file (.m4a, .mp3 or .wav)", type=["m4a", "mp3", "wav"])
if uploaded_file:
    # Save and convert audio to WAV format
    wav_path = convert_audio_to_wav(uploaded_file)

    with st.spinner("Transcribing..."):
        transcript, lang_detected = transcribe_audio(wav_path)
        st.subheader("Transcribed Text")
        st.write(transcript)

    with st.spinner("Translating..."):
        match mode:
            case "Hausa → English":
                src_lang = "ha"
                tgt_lang = "en"
            case "English → Hausa":
                src_lang = "en"
                tgt_lang = "ha"
            case "French → English":
                src_lang = "fr"
                tgt_lang = "en"
            case "English → French":
                src_lang = "en"
                tgt_lang = "fr"
            case "Afrikaans → English":
                src_lang = "af"
                tgt_lang = "en"
            case "English → Afrikaans":
                src_lang = "en"
                tgt_lang = "af"
        translation = translate_text(transcript, src_lang=src_lang, tgt_lang=tgt_lang)
        st.subheader("Translated Text")
        st.write(translation)

    # with st.spinner("Synthesising speech..."):
    #     tts_audio_path = synthesise_speech(translation, language=tgt_lang)
    #     st.audio(tts_audio_path, format="audio/wav")
