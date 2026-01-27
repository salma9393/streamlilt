import streamlit as st
from pydub import AudioSegment,silence
import speech_recognition as sr
recog=sr.Recognizer()
final_result=""
st.markdown("<h1>style='text-align':center;'>audio to text converter</h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
audio = st.file_uploader("Upload your audio file", type=["mp3", "wav"])

if audio:
    st.audio(audio)

    audio_segment = AudioSegment.from_file(
        audio, format=audio.type.split("/")[-1]
    )

if audio:
    st.audio(audio)
    audio_segment=AudioSegment.from_file(audio)
    chunks=silence.split_on_silence(audio_segment,min_silence_len=500,silence_thresh=audio_segment.dBFS - 20,keep_silence=100)
    for index,chunk in enumerate(chunks):
        chunk.export(str(index)+".wav",format="wav")
        with sr.AudioFile(str(index)+".wav")as source:
            recorded=recog.record(source)
            try:
                text=recog.recognize_google(recorded)
                final_result=final_result+" "+text
                print(text)
            except:
                print("None")
                final_result=final_result+"unaudible"
st.text_area(" ",value=final_result)    