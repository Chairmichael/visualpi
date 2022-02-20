#vis.py
# draws some dots with pygame

import pygame
from pygame.locals import *
import colorsys

def main():
	SIZE = 300
	pygame.init()
	BLACK = pygame.Color([0,0,0])

	colors = []
	for x in range(10):
		r,g,b = [round(i*255) for i in colorsys.hsv_to_rgb(x/10,0.8,0.8)]
		colors.append(pygame.Color(r,g,b))
	print(colors)
	dp = pygame.display.set_mode((SIZE*6,SIZE*6))
	pygame.display.set_caption("90k digits of pi -- Press any key to exit")
	lotsofpi = open('10Kpi.txt').read()
	for i in range(SIZE):
		for j in range(SIZE):
			if lotsofpi[j+i*SIZE] == lotsofpi[j+i*SIZE+1]:
				n = int(lotsofpi[j+i*SIZE])
				pygame.draw.circle(dp, colors[n], (j*6+2,i*6+2), 2)
				pygame.draw.circle(dp, colors[n], ((j+1)*6+2,i*6+2), 2)

	pygame.display.update()
	while True:
		for event in pygame.event.get():              
			if event.type == QUIT or event.type == KEYUP:
				pygame.quit()
				quit()
		pygame.time.Clock().tick(10)


if __name__ == '__main__':
	main()
