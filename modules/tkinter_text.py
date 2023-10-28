import random
import signal
import sys
import textwrap
import threading
import time
import tkinter as tk
from os import getenv
from queue import Queue

import pywintypes
import win32api
import win32con
from dotenv import load_dotenv
from googletrans import Translator

translator = Translator()
# from modules.audio_translate import translate_audio

load_dotenv()

OFFSET_X = 0
OFFSET_Y = 0.7
SUBTITLE_FONT_SIZE = int(getenv("SUBTITLE_FONT_SIZE"))
SUBTITLE_COLOR = getenv("SUBTITLE_COLOR")
SUBTITLE_BG_COLOR = getenv("SUBTITLE_BG_COLOR")
SACRIFICIAL_COLOR = getenv("SACRIFICIAL_COLOR")


def subtitle_updater(root: tk.Tk, queue, labels: [tk.Label]):
    # Check if there is something new in the queue to display.
    while not queue.empty():
        # destroy old label since new message inbound
        old_label = labels.pop(0)
        # old_label.destroy()
        if root.wm_state() == "withdrawn":
            # show root window
            root.deiconify()

        # create subtitle based on message in queue
        msg = queue.get()["format_text"]
        new_label = tk.Label(
            text=textwrap.fill(f"{msg}", 64),
            font=("Comic Sans MS", SUBTITLE_FONT_SIZE, "bold italic"),
            fg=SUBTITLE_COLOR,
            bg=SUBTITLE_BG_COLOR,
        )
        # hide root and destroy label after 3s
        label_time = 4000
        old_label.after(label_time, old_label.destroy)
        new_label.after(label_time, new_label.destroy)
        new_label.after(label_time, root.withdraw)

        # place subtitle at bottom middle of screen
        new_label.pack(side="top", anchor="n")
        # hWindow = pywintypes.HANDLE(int(old_label.master.frame(), 16))
        # # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
        # exStyle = (
        #     win32con.WS_EX_COMPOSITED
        #     | win32con.WS_EX_LAYERED
        #     | win32con.WS_EX_NOACTIVATE
        #     | win32con.WS_EX_TOPMOST
        #     | win32con.WS_EX_TRANSPARENT
        # )
        # win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        # hWindow = pywintypes.HANDLE(int(new_label.master.frame(), 16))
        # http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
        # The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.
        # exStyle = (
        #     win32con.WS_EX_COMPOSITED
        #     | win32con.WS_EX_LAYERED
        #     | win32con.WS_EX_NOACTIVATE
        #     | win32con.WS_EX_TOPMOST
        #     | win32con.WS_EX_TRANSPARENT
        # )
        # win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
        labels.append(new_label)
        root.update_idletasks()

    # run_interval = 50 # run every 0.05s
    run_interval = 50
    root.after(run_interval, lambda: subtitle_updater(root, queue, labels))


def setup_overlay():
    # set tkinter gui to be topmost without window
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry(
        f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+{OFFSET_X}+{round(root.winfo_screenheight()*OFFSET_Y)}"
    )
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)

    # Sacrifice random color for transparency
    root.wm_attributes("-transparentcolor", SACRIFICIAL_COLOR)
    root.config(bg=SACRIFICIAL_COLOR)

    # hide initial window
    root.withdraw()

    return root


def close_app(*_):
    print("Closing subtitler.")
    sys.exit(0)


def start_app(subtitle_queue):
    # catch keyboard interrupt to stop main thread
    signal.signal(signal.SIGINT, close_app)

    overlay = setup_overlay()
    subtitles = [tk.Label()]
    # subtitle_queue = Queue()

    # thread to listen and translate audio
    # threading.Thread(target=translate_audio, args=[subtitle_queue], daemon=True).start()

    # updates subtitles every 0.5s by checking queue
    subtitle_updater(overlay, subtitle_queue, subtitles)

    # set full-screen applications to borderless window for subtitles to appear over it
    overlay.mainloop()


if __name__ == "__main__":
    start_app()
