# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:16:38 2016

@author: paolo
"""
import pygame
from pygame.locals import *
import globalv
 
def draw_stick_figure(screen, x, y):
    pygame.draw.circle(screen, globalv.BLACK, [x, y],5)

def draw_root(screen,listpoints):
    for el in listpoints:
        print el[0]
        pygame.draw.circle(screen, globalv.BLACK, [int(el[0]), int(el[1])],1)
        
    