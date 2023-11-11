# VoiceAI

This project uses the Whisper.ai (more detail at [github.com/openai/whisper](github.com/openai/whisper)) model to transcribe audio and do multiple things with it.
All the translation is done through the [googletrans](https://pypi.org/project/googletrans/) library.
The program also uses [Tkinter](https://docs.python.org/3/library/tkinter.html) to show the subtitles on the screen.
To play the translated audio, a local [Coqui TTS](https://github.com/coqui-ai/TTS) server is set up to receive text and output audio file.
The [VB Audio cable software](https://vb-audio.com/Cable/) is also used to make the output of the device into an input source.

# Some use cases:

- ## Live subtitles

  Transcribed audio will be translated into the desired target language and shown on screen with Tkinter.

  ### Demo

  [live_subtitles.webm](https://github.com/RoyalHeart/VoiceAI/assets/75922889/95bf569d-1ebd-48cf-bf13-89530f0895ae)



- ## Speech to text to speech (dubbing with translation)

  Use Whisper.ai to transcribe your voice (or from an audio source) and use Coqui TTS to speak it. This works as a live vocal translation

## How to run

Make sure to have all the libraries installed and then just run the main.py file with the correct flags

If you use Windows, then you can try to make a batch file like the main.bat to activate a virtual environment and run the code

Some flags are useful such as --save_files because it stores the audio files temporarily and transcribes them one by one

### Run the live subtitles

An example command to run the live subtitles feature

```shell
python main.py --save_file --subtitles
```

### Run the dubbing translation

To run this feature, first run the TTS server, all the installation and setup can be found at [https://github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS):

```shell
tts-server --model_name "tts_models/en/vctk/vits" --use_cuda True
```

The models and the GPU option are up to you.
This config uses the GPU and the English model vits.

After the TTS server is running in the localhost, run this command to run the live dubbing feature

```shell
python main.py --save_file --dubbing
```

# Improvements

Some enhancements can be made such as:

- Use a better translation service such as DeepL for more natural translations
- Use native win32api to show text better
- Improve the threading, multiprocesses to run efficiently
- Try different thresholds for recording, and the interval for showing subtitles,...

# This project is inspired by these similar projects

- [A real-time translator by SociallyIneptWeeb](https://github.com/SociallyIneptWeeb/LanguageLeapAI)
- [Whisper mic](https://github.com/mallorbc/whisper_mic)
