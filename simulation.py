import random
from config import *
import math

class Particle:
    def __init__(self):
        self.x = SOURCE_X
        self.y = SOURCE_Y
        self.hit_x = None
        self.hit_y = None
        self.reached = False

    def move(self):
        angle = random.uniform(-0.05, 0.05)
        if USE_WAVE:
            slit_center = (SLIT1_Y + SLIT2_Y) / 2
            dy = self.y - slit_center
            angle += math.sin(dy * WAVE_FREQ) * WAVE_AMPLITUDE

        self.y += 2
        self.x += math.tan(angle) * 2

        if self.y >= DETECTOR_Y and not self.reached:
            self.hit_x = int(self.x)
            self.hit_y = DETECTOR_Y
            self.reached = True

class Simulation:
    def __init__(self):
        self.reset()

    def reset(self):
        self.particles = []
        self.hits = [0] * WIDTH
        global USE_WAVE
        USE_WAVE = True

    def toggle_mode(self):
        global USE_WAVE
        USE_WAVE = not USE_WAVE

    def update(self):
        if len(self.particles) < MAX_PARTICLES:
            self.particles.append(Particle())

        for p in self.particles:
            if not p.reached:
                p.move()
            else:
                if 0 <= p.hit_x < WIDTH:
                    self.hits[p.hit_x] += 1
                self.particles.remove(p)
