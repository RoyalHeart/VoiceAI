from time import sleep

from googletrans import Translator

translator = Translator()


def translate(input_queue, translation_queue, dest):
    while True:
        input = input_queue.get()
        translation = translator.translate(input, dest=dest)
        format_text = (
            f"[{translation.src}>{translation.dest}]:{translation.text}"
            if (translation.src != dest)
            else translation.text
        )
        print(format_text)
        translation_queue.put_nowait(
            {
                "text": translation.text,
                "format_text": format_text,
            }
        )
        sleep(0.1)
