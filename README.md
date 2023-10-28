# VoiceAI

This project use the Whisper.ai model to transcribe audio and do multiples thing with it.
All the translation is done through the googletrans library

Some use cases:

- # Live subtitles

  Transcibed audio will be translated into desired target language and show on screen with Tkinter.

  ## Demo

  [live_subtitles.webm](https://github.com/RoyalHeart/VoiceAI/assets/75922889/5abe5169-3981-4031-869d-4867c66ec83c)

- # Speech to text to speech (dubbing translation)[live_subtitles.webm](https://github.com/RoyalHeart/VoiceAI/assets/75922889/5abe5169-3981-4031-869d-4867c66ec83c)

  Use Whisper.ai to transcribe your voice (or from an audio source) and use Coqui TTS to speak it, can also for live vocal translation

## How to run

Make sure to have all the library installed and then just run the main.py file with the correct flags

If you use Windows, then you can try to make a batch file like the main.bat to activate a virtual environment and run the code

Some flags are useful such as --save_files because it store the audio files temporarily and transcribe one by one

### Run the live subtitles

An example command to run the live subtitles feature

```shell
python main.py --save_file --subtitles
```

### Run the dubbing translation

To run this feature, first run the TTS server:

```shell
tts-server --model_name "tts_models/en/vctk/vits" --use_cuda True
```

The models and gpu enabled are up to you.
This config works for me so I use it.

After the TTS server is running local host, run this command to run the live dubbing feature

```shell
python main.py --save_file --dubbing
```

## Improvements

Some enhancements can be made such as:

- Use a better translation service such as DeepL for more natural translation
- Use native win32api to show text better
- Improve the threading to be more efficiently
- Try different thresholds for record, show subtitles,...
