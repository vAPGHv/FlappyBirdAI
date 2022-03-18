"""------=made by vAPGHv=------"""

"""------=imports=------"""

import pygame as pyg # import pygame
from time import sleep
import random as rand
from colorama import init
from colorama import Fore, Back, Style # color for text

"""------=settings=------"""

init()

randl4AI = [1, 2, 3, 4, 5]
AIscore = 0
operacionscore = 0
goodoperacionscore = 0

FPS = 30

pyg.init()
clock = pyg.time.Clock()
choice = rand.choice
shuffle = rand.shuffle # random num

randl4AI2 = choice(randl4AI)

prug = pyg.draw.rect

vmar = [0, 200, 100, 50]
vmarchoice = choice(vmar)

"""------=colors=------"""

wblue = 0, 200, 255
green = 0, 255, 0
bgreen = 0, 100, 0
yellow = 255, 250, 0
oranje = 255, 200, 0
white = 255, 255, 255
black = 0, 0, 0

"""------=settings=------"""

v = 720
sh = 1080
centerv = v / 2
centersh = sh / 2
centervff = v / 2
centershff = sh / 2
centervmar = v / 2
centershmar = sh / 2

"""------=game=------"""

sc = pyg.display.set_mode((sh, v))
pyg.display.set_caption("test")

pyg.display.flip()

"""------=minicode=------"""

def bird():
    prug(sc, (yellow), (centershff-320, centervff, 50, 50))
    prug(sc, (oranje), (centershff-280, centervff+20, 20, 10))
    prug(sc, (white), (centershff-290, centervff+5, 10, 10))
    prug(sc, (black), (centershff-287, centervff+7, 5, 5))

def mar():

    """------=up=------"""

    prug(sc, (green), (centershmar * 2, vmarchoice + -centervmar + 130, 100, centerv))

    """------=down=------"""

    prug(sc, (green), (centershmar * 2, vmarchoice + centervmar + 30, 100, centerv))

def st():

    """------=up=------"""

    if centervff <= vmarchoice + -centervmar + 500:
        if centershff - 320 == centershmar * 2:
            game_over()
        elif centershff - 320 - 80 == centershmar * 2:
            game_over()
        elif centershff - 320 - 40 == centershmar * 2:
            game_over()

    """------=down=------"""

    if centervff >= vmarchoice + centervmar + 30:
        if centershff - 320 == centershmar * 2:
            game_over()
        elif centershff - 320 - 80 == centershmar * 2:
            game_over()
        elif centershff - 320 - 40 == centershmar * 2:
            game_over()

"""------=code=------"""

while True:

    def game_over():
        scoreAI = goodoperacionscore / operacionscore * 100
        print(f"\n\n\n\n\n\n\n\n    {Fore.CYAN}------=operations=------{Style.RESET_ALL}\n\n   Operation: {operacionscore}\n   Successful operations: {goodoperacionscore}")
        if scoreAI >= 70:
            print(Fore.GREEN + "Percentage of successful operations: %.2f (GOOD!!!)" % scoreAI)
        elif scoreAI <= 69 and scoreAI >= 37:
            print(Fore.YELLOW + "Percentage of successful operations: %.2f (ok?..)" % scoreAI)
        else:
            print(Fore.RED + "Percentage of successful operations: %.2f (BAD!)" % scoreAI)
        sleep(1)
        pyg.quit()
        exit()

    AIIF = centervff > vmarchoice + centervmar - 50

    """------=exit and jump=------"""

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            game_over()

    """------=AI=------"""

    if AIIF:
        if randl4AI2 == 4 or randl4AI2 == 2:
            operacionscore += 1
            centervff -= 130
            randl4AI2 = choice(randl4AI) # random number from the list
            print(f"{Fore.GREEN}Верно: {randl4AI2}{Style.RESET_ALL}")
            goodoperacionscore += 1
            print(Style.RESET_ALL + f"Номер операции: {operacionscore}")
        else:
            if AIscore >= 6:
                print(Fore.RED + f"Неверный {Fore.BLUE}(помощь){Fore.RED} : {randl4AI2}")
                print(Style.RESET_ALL + f"Номер операции: {operacionscore}")
                operacionscore += 1
                randl4AI2 = 4
                AIscore = 0
            else:
                operacionscore += 1
                print(Fore.RED + f"Неверный: {randl4AI2}")
                randl4AI2 = choice(randl4AI)
                print(Style.RESET_ALL + f"Номер операции: {operacionscore}")
                AIscore += 1

    """------=gravitacion and motion=------"""

    centervff += 12
    centershmar -= 10

    """------=respawn=------"""

    if centershmar == -100:
        vmarchoice = choice(vmar)
        centershmar = centersh

    """------=game over=------"""

    if centervff >= v-78:
        game_over()
    elif centervff <= -25:
        game_over()

    """------=fon=------"""

    sc.fill(wblue)

    """------=codes=------"""

    bird()
    mar()
    st()

    """------=fon=------"""

    prug(sc, (bgreen), (0, v-20, sh+100, 50 ))
    prug(sc, (bgreen), (0, -20, sh+100, 50 ))
    pyg.display.update()
    clock.tick(FPS)
