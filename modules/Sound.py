import sounddevice

from modules.AudioContent import AudioContent
from modules.Coqui_TTS import TTS, fetch_TTS

MICROPHONE_ARRAY_ID = 1
CABLE_OUTPUT_ID = 2
CABLE_INPUT_ID = 5
HEADPHONES_OUTPUT_ID = 4


def playToOutput(audioContent: AudioContent, deviceId=4):
    print("Frame rate: " + str(audioContent.frameRate))
    sounddevice.play(audioContent.audio, audioContent.frameRate, device=deviceId)
    sounddevice.wait()


print(sounddevice.query_devices())
message = "WHAT ARE YOU DOING? START DOING SOMETHING AND STOP PLAYING!"
# playToOutput(TTS(message))
# playToOutput(fetch_TTS(message))
