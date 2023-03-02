import pygame, sys
from player import *
from draw_lines import *
from dianoite import dia_
from draw_map import draw_m
from enimigo import draw_enim
from vida import draw_vida

pygame.font.init()
pygame.display.init()

#variaveis da tela

altura_tela = 600
largura_tela = 810
tamanho_tela = (largura_tela,altura_tela)
tela = pygame.display.set_mode(tamanho_tela)

#outras variaveis
fps = 15
rodando = True
font = pygame.font.Font(None,32)
k = pygame.key

def tela_update():
	tela.fill((0,0,0))
	draw_m(tela)
	player(k.get_pressed(),tela)
	draw_enim(tela)
	draw(tela,tamanho_tela)
	draw_map(tela)
	draw_vida(tela)

while rodando:

	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()
			rodando = False

	tela_update()
	dia_(tela)
	texto = pygame.font.Font.render(font,"X=" + str(player_position[0]) + "«»" + "Y=" + str(player_position[1]),1,(255,255,255))
	tela.blit(texto,(30,13))
	pygame.display.flip()
	pygame.time.Clock().tick(fps)

pygame.display.quit()

