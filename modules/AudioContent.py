import numpy as np


class AudioContent:
    def __init__(self, audio: np.ndarray, frameRate: int):
        self.audio = audio
        self.frameRate = frameRate
