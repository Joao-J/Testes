import pygame
from map import data_l1
tiles = pygame.Surface((30,30))
def draw_m(tela):
	y = 0
	for i in data_l1:
		x = 0
		for z in i:
			if z[0] >= 5:
				if z[1] == 2:
					tiles.fill((255,0,0))
				else:
					tiles.fill((124,124,124))
			elif z[0] == 25:
				if z[1] == 1:
					tiles.fill((100,100,100))
				else:
					tiles.fill((255,100,100))
			else:
				tiles.fill((0,255,0))

			tela.blit(tiles,(x * 30,y * 30))
			x += 1
		y += 1
