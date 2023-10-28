import random
from queue import Queue
from threading import Thread
from time import sleep

from tkinter_text import start_app


def update(queue):
    while True:
        rand_int = random.randint(1, 5)
        sleep(rand_int)
        queue.put_nowait(f"{random.random()}hello  {rand_int}")


queue = Queue()
Thread(target=update, args=[queue]).start()
start_app(queue)
