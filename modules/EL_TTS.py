from os import getenv
import io
import requests
from dotenv import load_dotenv
from pydub import AudioSegment
import numpy as np
from .AudioContent import AudioContent

load_dotenv()
EL_KEY = getenv('EL_KEY')
EL_VOICE = getenv('EL_VOICE')


def EL_TTS(message) -> AudioContent:
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{EL_VOICE}'
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': EL_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'text': message,
        'voice_settings': {
            'stability': 0.75,
            'similarity_boost': 0.75
        }
    }
    response = requests.post(url, headers=headers, json=data, stream=True)
    audioSegment: AudioSegment = AudioSegment.from_file(
        io.BytesIO(response.content), format="mp3")
    arr = np.ndarray((int(audioSegment.frame_count()), audioSegment.channels),  # type: ignore
                     buffer=audioSegment.raw_data, dtype=np.int16)  # type: ignore
    audioContent = AudioContent(arr, audioSegment.frame_rate)  # type: ignore
    return audioContent
