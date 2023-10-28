# import numpy as np
import sounddevice

MICROPHONE_ARRAY_ID = 1
CABLE_OUTPUT_ID = 2
CABLE_INPUT_ID = 5
HEADPHONES_OUTPUT_ID = 4


def play_to_output(audio, frame_rate, deviceId=8):
    sounddevice.play(audio, frame_rate, device=deviceId)
    # sounddevice.wait()


# if __name__ == "__main__":
#     try:
#         print(sounddevice.query_devices())
#         message = "WHAT ARE YOU DOING? START DOING SOMETHING AND STOP PLAYING!"
#         (audio_array, frame) = get_tts(message)
#         play_to_output(audio=audio_array, frame_rate=frame)
#     except Exception as e:
#         print(e)
