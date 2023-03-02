import pygame
from random import randint
from player import player_position
from dianoite import tempo
from map import enimigo_analise, set_data, colision
from vida import vidas

enimigox = []
enimigo_pele = pygame.Surface((30,30))
enimigo_pele.fill((255,130,50))
tmp_spaw = 0

def ativ_enim():
	achou = False
	if len(enimigox) <= 9:
		if randint(1,20) < 10:
			while not achou:
				x = randint(0,26)
				y = randint(0,19)
				achou = enimigo_analise(y,x)
				if achou:
					enimigox.append([x,y])
			#print("passou2")

def enimigo_run():

	global enimigox
	x = 0
	#print("passou0")
	if tempo[1] >= 16:
		ativ_enim()
		#print("passou1")
	for e in enimigox:
		if tempo[1] >= 18 or tempo[1] <= 8:
			move_enimigo(e,x)
		x += 1

	if tempo[1] == 8:
		enimigox = []


def draw_enim(tela):
	global tmp_spaw

	if tmp_spaw < 5:
		tmp_spaw += 1
	else:
		tmp_spaw = 0
		enimigo_run()

	for eni in enimigox:
		x,y = eni
		tela.blit(enimigo_pele,(x * 30,y * 30))

def move_enimigo(eni,x):
	global vidas
	jx,jy = player_position
	jx = int(jx/30)
	jy = int(jy/30)

	xy = eni[0] - 3

	vl_x = 0
	vl_y = 0

	while xy < eni[0] + 4:
		if jx == xy:
			if xy > eni[0]:
				vl_x = 1
			else:
				vl_x = -1

		xy = xy + 1

	xy = eni[1] - 3

	while xy < eni[1] + 4:
		if jy == xy:
			if xy > eni[1]:
				vl_y = 1
			else:
				vl_y = -1
		xy = xy + 1
	xenim = eni[0] + vl_x
	yenim = eni[1]

	if colision(0,(0,0),xenim,yenim):
		enimigox[x] = (xenim, yenim)
	else:
		xenim -= vl_x
	yenim += vl_y

	if colision(0,(0,0),xenim,yenim):
		enimigox[x] = (xenim, yenim)

	if xenim == jx and yenim == jy:
		vidas -= 1
		print(vidas)
