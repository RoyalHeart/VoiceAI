import io
import os
from os import getenv

import numpy as np
import requests
from dotenv import load_dotenv
from pydub import AudioSegment

# from .audio_content import AudioContent

load_dotenv()

TTS_MODEL_TACOTRON2: str = "tts_models/en/ljspeech/tacotron2-DDC"
TTS_MODEL_VITS: str = "tts_models/en/vctk/vits"
TTS_VITS_VOICE = getenv("TTS_VITS_FEMALE_VOICE")


def get_tts(message: str) -> tuple[np.ndarray, int]:
    url = f"http://localhost:5002/api/tts"
    headers = {"accept": "audio/wav", "Content-Type": "application/json"}
    data = {
        "text": message,
        "speaker_id": TTS_VITS_VOICE,
    }
    response = requests.get(url, headers=headers, params=data, stream=True)
    audioSegment: AudioSegment = AudioSegment.from_wav(io.BytesIO(response.content))
    audio_array = np.ndarray(
        (int(audioSegment.frame_count()), audioSegment.channels),  # type: ignore
        buffer=audioSegment.raw_data,
        dtype=np.int16,
    )  # type: ignore
    return (audio_array, audioSegment.frame_rate)


def tts(message: str, model=TTS_MODEL_VITS) -> tuple[np.ndarray, int]:
    wavFileOutput = f'./temp/{TTS_VITS_VOICE}_{message.replace(" ", "_").replace("?","").replace("!", "")}.wav'
    print("TTS message: {}".format(message))
    os.system(
        f'tts --text "{message}" --model_name {model} --speaker_idx {TTS_VITS_VOICE} --out_path {wavFileOutput} --use_cuda True'
    )
    audioSegment: AudioSegment = AudioSegment.from_wav(wavFileOutput)
    arr = np.ndarray(
        (int(audioSegment.frame_count()), audioSegment.channels),  # type: ignore
        buffer=audioSegment.raw_data,
        dtype=np.int16,
    )  # type: ignore
    # audioContent = AudioContent(arr, audioSegment.frame_rate)  # type: ignore
    return (arr, audioSegment.frame_rate)
