
import keyboard
import pyaudio
import numpy as np
import threading
import time

class keyboard:
    def constructer(self):
        self.KEY = {


            49: 0x1, #1
            50: 0x2, #2
            51: 0x3, # 3
            52: 0xc, # 4
            81: 0x4, # Q
            87: 0x5, # W
            69: 0x6, # E
            82: 0xD, # R
            65: 0x7, # A
            83: 0x8, # S
            68: 0x9, # D
            70: 0xE, # F
            90: 0xA, # Z
            88: 0x0, # X
            67: 0xB, # C
            86: 0xF  # V
        }

        self.keyPressed = []
        self.nextKey = None

    def keyPressed(self, keycode):
        return self.keysPressed[self.keyCode]

    def keyboardEvent(self):

            while True:
                if keyboard.is_pressed(self.key) and self.nextKey is not None:
                    self.nextKey(self.KEY)
                    self.nextKey = None


class Speaker:
    def __init__(self, frequency=440):
        self.p = pyaudio.PyAudio()
        self.frequency = frequency  # Tone frequency in Hz
        self.volume = 0.5
        self.running = False
        self.thread = None

    def _generate_tone(self):
        # Create a stream
        stream = self.p.open(format=pyaudio.paFloat32,
                             channels=1,
                             rate=44100,
                             output=True)
        sample_rate = 44100
        duration = 0.1  # seconds per chunk
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        wave = np.sin(2 * np.pi * self.frequency * t).astype(np.float32)

        while self.running:
            stream.write(self.volume * wave)

        stream.stop_stream()
        stream.close()

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._generate_tone)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()

    def terminate(self):
        self.p.terminate()

# Example usage (like CHIP-8 style beep)
if __name__ == "__main__":
    speaker = Speaker(frequency=880)  # CHIP-8 beep is around 880 Hz
    speaker.start()
    time.sleep(0.5)  # Play beep for 0.5 second
    speaker.stop()
    speaker.terminate()
