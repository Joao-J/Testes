import pygame

pygame.font.init()

tempo = ["dia",12]

ceu = pygame.Surface((810,600))
ceu_brilho = 0

font = pygame.font.Font(None,30)

segundos = 0

def dia_(tela):
	global tempo,segundos,ceu_brilho
	t = ""
	x = 0
	min = ""
	hr = ""

	if (segundos*3) < 10:
		min = "0"+str(segundos*3)
	else:
		min = str(segundos*3)

	if tempo[1] < 10:
		hr = "0" + str(tempo[1])
	else: hr = str(tempo[1])

	t = "HORARIO { " + hr + ":" + min + " }"

	if tempo[1] == 24:
		tempo[1] = 1

	if tempo[1] <= 8:
		ceu_brilho = 8 - tempo[1]
	elif tempo[1] > 16:
		ceu_brilho =  tempo[1] - 15

	segundos += 1

	if segundos == 20:
		tempo[1] += 1
		segundos = 0

	#print((40*ceu_brilho))
	texto = pygame.font.Font.render(font,t,1,(255,255,255))
	ceu.fill((15,15,180))
	ceu.set_alpha((14*ceu_brilho))
	tela.blit(ceu,(0,0))
	tela.blit(texto,(810 - (texto.get_width() + 30),13))
