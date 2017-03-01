import pygame, sys, Button, Board, Player
from pygame.locals import *

pygame.init()

#Creating the display surface
DISPLAYSURF = pygame.display.set_mode((1024,720))
pygame.display.set_caption("Monopoly")
DISPLAYSURF.fill((255,255,255))

#Drawing the black outline around the game
pygame.draw.line(DISPLAYSURF, (0,0,0), (10,20), (10,700), 5)
pygame.draw.line(DISPLAYSURF, (0,0,0), (10,700), (790,700) ,5)
pygame.draw.line(DISPLAYSURF, (0,0,0), (790,700), (790,20), 5)
pygame.draw.line(DISPLAYSURF, (0,0,0), (790,20), (10,20), 5)

#Display image of board
boardimg = pygame.image.load('board.jpg')
boardx = 30
boardy = 30
DISPLAYSURF.blit(boardimg,(boardx,boardy))

#Make the buttons
buy = Button.Button(DISPLAYSURF,820,200,120,60,"Buy")
sell = Button.Button(DISPLAYSURF,820,120,120,60,"Sell")
roll = Button.Button(DISPLAYSURF,820,40,120,60,"Roll")
endturn = Button.Button(DISPLAYSURF,820,280,120,60,"End turn")

#Make the board
board = Board.Board()

#make a player
player1 = Player.Player(DISPLAYSURF,(160,30,160),0,board)
player2 = Player.Player(DISPLAYSURF,(30,30,30),1,board)


#main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if buy.pressed(pygame.mouse.get_pos()):
                #buy func goes here
                print("buy")
            elif sell.pressed(pygame.mouse.get_pos()):
                #sell function goes here
                print("sell")
            elif roll.pressed(pygame.mouse.get_pos()):
                #roll function goes here
                print("Roll")
            elif endturn.pressed(pygame.mouse.get_pos()):
                #end turn func goes here
                print("End turn")
            print(pygame.mouse.get_pos())
    pygame.display.update()
