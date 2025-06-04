import pygame
import sys
import random


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Sys")
font = pygame.font.SysFont("Courier", 32, bold=True)
clock = pygame.time.Clock()


rouge = (255, 0, 0)
noir = (0, 0, 0)


messages = [
    "⚠️ natrixIsBack ⚠️",
    "FAKE VIRUS AHAH",
    "TYPE 'F' TO CLOSE",
    "TROLL YOUR FRIENDS",
    "USE CREDITS...",
    "SYSTEM HACKED...",
    "ALL FILES DELETED...",
    "ERROR : 0xDEADBEEF"
]

def afficher_message(msg, y_offset):
    texte = font.render(msg, True, rouge)
    rect = texte.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset))
    screen.blit(texte, rect)


running = True
clignote = True
while running:
    screen.fill(noir)

   
    if clignote:
        for i, message in enumerate(messages):
            afficher_message(message, i * 50 - 150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_f:
                running = False

    clignote = not clignote
    pygame.display.flip()
    clock.tick(20)  

pygame.quit()
sys.exit()
