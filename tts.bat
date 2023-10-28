CD %cd%
start "TTS" conda activate voiceai ^&^& tts-server --model_name "tts_models/en/vctk/vits" --use_cuda True