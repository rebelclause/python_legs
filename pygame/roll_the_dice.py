#!/usr/bin/env python3

'''
Created on Aug 14, 2018

@author: Tim Pozza
@email: rebelclause@gmail.com
'''
import pygame, sys
from pygame.locals import *



players = {'you': {'rolltotal': None, 'otherstuff': None }, 'me': {'rolltotal': None, 'otherstuff': None}}

size = width, height = 256, 256
white = 255, 255, 255
grey = 128, 129, 127
black = 0, 0, 0

pygame.init()
DISPLAYSURF = pygame.display.set_mode((size), 0, 32)
DISPLAYSURF.fill(white)
pygame.display.update()

def reviewvals():
    global players
    print('Number of players: ', len(players)) # only counts the primary keys, the players                
    for player, attribdict in players.items():
        for key, value in attribdict.items():
            print(f"{player}: {key} = {value}")
    # just in case later we want to ask players for their names and players is empty
    try:
        players = {k: players[k] for k in sorted(players, key=lambda x: players[x]['rolltotal'], reverse=True)}
    except:
        pass
    finally:
        if players:
            return players
        else:
            pass
    
def rolldice():
    from random import choice
    select = [1, 2, 3, 4, 5, 6]
    select = choice(select)
    # sets the properties of the circle
    pos = {'1': [(128, 128)],
           '2': [(64, 64), (192, 192)],
           '3': [(51, 51), (128, 128), (205, 205)],
           '4': [(64, 64), (64, 192), (192, 64), (192, 192)],
           '5': [(51, 51), (51, 205), (128, 128), (205, 205), (205, 51)],
           '6': [(64, 64), (64, 128), (64, 192), (192, 64), (192, 128), (192, 192)],
           'radius': 12,
           'width': 11}
    DISPLAYSURF.fill(white)
    for x in range(select):
        # draws the circle
        val = str(select)
        pygame.draw.circle(DISPLAYSURF, grey, pos[val][x-1], pos['radius'] + 5, pos['width'])
        pygame.draw.circle(DISPLAYSURF, black, pos[val][x-1], pos['radius'], pos['width'])
    pygame.display.update()
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

def update(chance, player):
    rolltotal = players[player]['rolltotal']
    if rolltotal == None:
        players[player]['rolltotal'] = chance
    else:
        players[player]['rolltotal'] = rolltotal + chance
    print('dice released')  
    print(f"{player} rolltotal: {players[player]['rolltotal']}")

def cleanup(count):
    if count < len(players):
        print('Exiting early.')
    DISPLAYSURF.fill(black)
    pygame.display.flip()
    try:
        pygame.quit()
        sys.exit()
    finally:
        pygame.quit()
        sys.exit()
            
def surfask():
    count = len(players) - len(players)
    for player in players.keys():
        name = f"\nPlayer {count}'s name: {player}"
        print(name)
        rolls = 0
        while rolls < 5:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
                    cleanup(count)
                if event.type == KEYDOWN:
                    print('warming dice -- ready to throw')
                    handle(event)
                    
                    chance = rolldice()
                    update(chance, player)
                    rolls = rolls + 1
                    
        count = count + 1

    print('\n## Review ##')
    print(reviewvals())
    cleanup(count)

print('\n## Roll ##')
reviewvals()
surfask()
