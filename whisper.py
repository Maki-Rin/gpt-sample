from io import BytesIO
import openai
import speech_recognition as sr
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

r = sr.Recognizer()

def voice_to_text():
    with sr.Microphone(sample_rate=16000) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Done!")
        audio_data = BytesIO(audio.get_wav_data())
        audio_data.name = "from_mic.wav"
        transcript = openai.Audio.transcribe("whisper-1", audio_data, language="ja")
        return transcript['text']