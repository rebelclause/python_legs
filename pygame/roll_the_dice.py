#!/usr/bin/env python3

'''
Created on Aug 14, 2018

@author: Tim Pozza
@email: rebelclause@gmail.com
'''

players = {'you': {'rolltotal': None, 'otherstuff': None }, 'me': {'rolltotal': None, 'otherstuff': None}}
size = width, height = 256, 256
white = 255, 255, 255
black = 0, 0, 0

import pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((size), 0, 32)
DISPLAYSURF.fill(white)
pygame.display.update()

def reviewvals():
    print('Number of players: ', len(players)) # only counts the primary keys, the players                
    for player, attribdict in players.items():
        for key, value in attribdict.items():
            print(player, key, value)

def rolldice():
    from random import choice
    select = [1, 2, 3, 4, 5, 6]
    select = choice(select)
    return select

def handle(event):
    DISPLAYSURF.fill(black)
    pygame.display.update()
    while event.type == KEYDOWN:
        for event in pygame.event.get():
            if event.type == KEYUP:
                return
            else:
                pass # start a timer and warn the player with a countdown when the roll will kick off
def surfask():
    count = 1
    for player in players.keys():
        name = f"Player {count}'s name: {player}"
        print(name)
        rolls = 0
        while rolls < 2:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
                    pygame.quit()
                if event.type == KEYDOWN:
                    print('warming dice -- ready to throw')
                    handle(event)
                    DISPLAYSURF.fill(white)
                    pygame.display.update()
                    chance = rolldice()
                    rolltotal = players[player]['rolltotal']
                    if rolltotal == None:
                        players[player]['rolltotal'] = chance
                    else:
                        players[player]['rolltotal'] = rolltotal + chance
                    print('dice released')  
                    print(f"{player} rolltotal: {players[player]['rolltotal']}")
                    rolls = rolls + 1
        count = count + 1
    pygame.quit()

print('## Then ## \n')
reviewvals()
surfask()
print('## Now ## \n')
reviewvals()


    