import whisper
import io
from pydub import AudioSegment
from modules.EL_TTS import EL_TTS
from modules.Coqui_TTS import fetch_TTS
import speech_recognition as sr
import whisper
import queue
import tempfile
import os
import threading
import click
import torch
import numpy as np

from modules.Sound import playToOutput


@click.command()
@click.option("--model",
              default="base",
              help="Model to use",
              type=click.Choice(["tiny", "base", "small", "medium", "large"]))
@click.option("--english",
              default=False,
              help="Whether to use English model",
              is_flag=True,
              type=bool)
@click.option("--verbose",
              default=False,
              help="Whether to print verbose output",
              is_flag=True,
              type=bool)
@click.option("--energy",
              default=1000,
              help="Energy level for mic to detect",
              type=int)
@click.option("--dynamic_energy",
              default=False,
              is_flag=True,
              help="Flag to enable dynamic engergy",
              type=bool)
@click.option("--pause",
              default=0.8,
              help="Pause time before entry ends",
              type=float)
@click.option("--save_file",
              default=False,
              help="Flag to save file",
              is_flag=True,
              type=bool)
def main(model, english, verbose, energy, pause, dynamic_energy, save_file):
    temp_dir = tempfile.mkdtemp() if save_file else None
    # there are no english models for large
    if model != "large" and english:
        model = model + ".en"
    print("Load model...")
    audio_model = whisper.load_model(model)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()
    print("Start record...")
    threading.Thread(target=record_audio,
                     args=(audio_queue, energy, pause, dynamic_energy,
                           save_file, temp_dir)).start()
    print("Start transcribe...")
    threading.Thread(target=transcribe_forever,
                     args=(audio_queue, result_queue, audio_model, english,
                           verbose, save_file)).start()

    while True:
        result = result_queue.get()
        print("You say:", result)
        audioContent = fetch_TTS(result)
        playToOutput(audioContent)


def record_audio(audio_queue, energy, pause, dynamic_energy, save_file,
                 temp_dir):
    # load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=5)
        i = 0
        while True:
            # get and save audio to wav file
            print("Listening...")
            audio = r.listen(source)
            if save_file:
                data = io.BytesIO(audio.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                filename = os.path.join(temp_dir, f"temp{i}.wav")
                print(filename)
                audio_clip.export(filename, format="wav")
                audio_data = filename
            else:
                torch_audio = torch.from_numpy(
                    np.frombuffer(audio.get_raw_data(),
                                  np.int16).flatten().astype(np.float32) /
                    32768.0)
                audio_data = torch_audio

            audio_queue.put_nowait(audio_data)
            i += 1


def transcribe_forever(audio_queue, result_queue, audio_model, english,
                       verbose, save_file):
    while True:
        audio_data = audio_queue.get()
        if english:
            result = audio_model.transcribe(audio_data, language='english')
        else:
            result = audio_model.transcribe(audio_data)

        if not verbose:
            predicted_text = result["text"]
            result_queue.put_nowait(predicted_text)
        else:
            result_queue.put_nowait(result)
        if save_file:
            os.remove(audio_data)


main()
