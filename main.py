import pygame
from config import *
from simulation import Simulation
from renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wave-Particle Duality Simulation")
clock = pygame.time.Clock()

sim = Simulation()
renderer = Renderer(screen, sim)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                sim.reset()
            elif event.key == pygame.K_SPACE:
                sim.toggle_mode()

    sim.update()
    renderer.draw()

pygame.quit()
