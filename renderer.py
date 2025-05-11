from config import *
import pygame

class Renderer:
    def __init__(self, screen, simulation):
        self.screen = screen
        self.sim = simulation

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        pygame.draw.rect(self.screen, SLIT_COLOR, (SLIT_X, SLIT1_Y, SLIT_WIDTH, SLIT_HEIGHT))
        pygame.draw.rect(self.screen, SLIT_COLOR, (SLIT_X, SLIT2_Y, SLIT_WIDTH, SLIT_HEIGHT))

        pygame.draw.line(self.screen, DETECTOR_COLOR, (0, DETECTOR_Y), (WIDTH, DETECTOR_Y), 2)

        for x, h in enumerate(self.sim.hits):
            if h > 0:
                pygame.draw.line(self.screen, HIT_COLOR, (x, DETECTOR_Y), (x, DETECTOR_Y - h))

        for p in self.sim.particles:
            pygame.draw.circle(self.screen, PARTICLE_COLOR, (int(p.x), int(p.y)), 2)

        font = pygame.font.SysFont(None, 24)
        mode = "Wave" if USE_WAVE else "Particle"
        text = font.render(f"Mode: {mode}  [Press SPACE to toggle, R to reset]", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

        pygame.display.flip()
