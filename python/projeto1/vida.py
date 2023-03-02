import pygame
vidas = 25

def draw_vida(tela):
	for i in range(vidas):
		vidad = pygame.Surface((10,10))
		vidad.fill((255,0,0))
		tela.blit(vidad,(20 + (10 * i),50))
