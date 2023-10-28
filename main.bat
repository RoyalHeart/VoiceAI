cd %cd%
@REM call ./tts.bat
start "sttts" conda activate voiceai ^&^& python main.py --save_file --verbose --subtitles  --dest "vi"