from .Coqui_TTS import fetch_TTS
from .Coqui_TTS import TTS
from .AudioContent import AudioContent
import sounddevice

MICROPHONE_ARRAY_ID = 1
CABLE_OUTPUT_ID = 2
CABLE_INPUT_ID = 5
HEADPHONES_OUTPUT_ID = 4


def playToOutput(audioContent: AudioContent, deviceId=CABLE_INPUT_ID):
    # print(sounddevice.query_devices())
    print("Frame rate: " + str(audioContent.frameRate))
    sounddevice.play(audioContent.audio,
                     audioContent.frameRate, device=deviceId)
    sounddevice.wait()


# message = "WHAT ARE YOU DOING? START DOING SOMETHING AND STOP PLAYING!"
# playToOutput(TTS(message))
# playToOutput(fetch_TTS(message))
