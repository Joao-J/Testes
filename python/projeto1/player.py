import pygame
from map import *

#player
player_position = [0,0]
player_wide = [30,30]
#visao
visao_di = [0,0]
visao_pos = [0,0]
visao_n = [0,0]
player_vi = True
#outras
p = pygame

def player(b,tela):

	if b[p.K_a] and player_position[0] > 0 and colision(visao_n[0],(player_position),-1,0):
		if visao_n[0] == 1:
			player_position[0] -= player_wide[0]
	if b[p.K_d] and player_position[0] < 780 and colision(visao_n[0],(player_position),1,0):
		if visao_n[0] == 2:
			player_position[0] += player_wide[0]
	if b[p.K_w] and player_position[1] > 0 and colision(visao_n[0],(player_position),0,-1):
		if visao_n[0] == 3:
			player_position[1] -= player_wide[1]
	if b[p.K_s] and player_position[1] < 570 and colision(visao_n[0],(player_position),0,1):
		if visao_n[0] == 4:
			player_position[1] += player_wide[1]
	if b[p.K_e]:
		useordrop(1)
	if b[p.K_q]:
		useordrop(-1)
	if b[p.K_i]:
		useordrop(2)

	player = pygame.Surface(player_wide)
	player.fill((255,255,255))
	tela.blit(player,player_position)

	if player_vi == True:
		player_olhar(b,tela)

def player_olhar(b,tela):
	global visao_di, visao_pos,visao_n
	if b[p.K_a]:
		visao_di = [10,30]
		visao_pos = player_position
		visao_n = [1,-1]
	if b[p.K_d]:
		visao_di = [10,30]
		visao_pos = [player_position[0]+20,player_position[1]]
		visao_n = [2,1]
	if b[p.K_w]:
		visao_di = [30,10]
		visao_pos = player_position
		visao_n = [3,-1]
	if b[p.K_s]:
		visao_di = [30,10]
		visao_pos = [player_position[0], player_position[1] + 20]
		visao_n = [4,1]
	olhar = pygame.Surface(visao_di)
	olhar.fill((0,0,255))

	tela.blit(olhar,visao_pos)


def useordrop(n):
	ye = 0
	xe = 0
	vl = 0
	if 3 > visao_n[0] > 0:
		xe = visao_n[1]
	elif  2 < visao_n[0] > 0:
		ye = visao_n[1]
	y = (int(visao_pos[1]/30)) + ye
	x = (int(visao_pos[0]/30)) + xe
	dt = data()[y][x][0]
	if dt >= 99 and n == 1:
		dt = -1
	if n == -1 and dt == 0:
		n = 0

	if n == 2:
		n = 0

	if dt + n > 10:
		vl = 2

	if n == 0 and 10 >= dt >= 5:
		if data()[y][x][1] == 2:
			vl = 1
		else:
			vl = 2

	set_data(y, x,[(dt + n),vl])
