# audio.py
import pygame
import random
from .config import CHEER_SOUNDS, DEFAULT_VOLUME

class AudioManager:
    def __init__(self):
        pygame.mixer.init()

        self.sounds = [
            pygame.mixer.Sound(str(path))
            for path in CHEER_SOUNDS
        ]

        self.volume = DEFAULT_VOLUME
        self._apply_volume()

        self.last_sound = None

    def _apply_volume(self):
        for sound in self.sounds:
            sound.set_volume(self.volume)

    def set_volume(self, value: float):
        self.volume = max(0.0, min(1.0, value))
        self._apply_volume()

    def play_random(self):
        # 🚫 prevent overlap
        if pygame.mixer.get_busy():
            return

        sound = random.choice(self.sounds)

        # 🚫 avoid repeating the same sound twice
        if sound == self.last_sound and len(self.sounds) > 1:
            sound = random.choice(
                [s for s in self.sounds if s != self.last_sound]
            )

        sound.play()
        self.last_sound = sound
