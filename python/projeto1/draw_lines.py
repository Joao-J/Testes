import pygame
from map import data
from player import player_position
from draw_map import draw_m

pygame.font.init()

tamanho = 30
branco = (255,255,255)
font = pygame.font.Font(None,20)

def draw(tela,tt):
	lateral = 0.0
	altura = 0.0
	l,a = tt

	while lateral < (l / tamanho)-1:
		lateral += 1
		p1,p2 = (((lateral  * tamanho),0),((lateral * tamanho), a))
		pygame.draw.line(tela,branco,p1,p2)

	while altura < (a/tamanho) -1:
		altura += 1
		p1,p2 = ((0,(altura*tamanho)),(l,(altura*tamanho)))
		pygame.draw.line(tela,branco,p1,p2)

def draw_map(tela):
	yy = 0
	for i in data():
		xx = 0
		for x in i:
			if player_position == [xx*30,yy*30]:
				branco = (0,0,0)
			else:
				branco = (255,255,255)

			texto = pygame.font.Font.render(font,str(x[0]),1,(branco))
			tela.blit(texto,((xx*30)+10,(yy * 30) + 2))
			xx += 1
		yy += 1

