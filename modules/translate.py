from os import getenv
from time import sleep

from dotenv import load_dotenv
from googletrans import Translator

translator = Translator()

load_dotenv()
TRANSLATION_DESTINATION_LANGUAGE = getenv("TRANSLATION_DESTINATION_LANGUAGE", "en")


def translate(input_queue, translation_queue, dest):
    print("Start translating thread...")
    while True:
        input = input_queue.get()
        translation = translator.translate(input, dest=dest)
        translation_text = (
            f"[{translation.src}>{translation.dest}]: {translation.text}"
            if (translation.src != translation.dest)
            else ""
        )
        translation_queue.put_nowait(
            {
                "origin": translation.origin,
                "translation": translation.text,
                "translation_format": translation_text,
            }
        )
