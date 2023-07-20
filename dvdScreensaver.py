import sys 
import pygame
pygame.init()   

clock = pygame.time.Clock() 
info = pygame.display.Info() 
monitorx, monitory = info.current_w, info.current_h
fps = 300

BLACK = ( 0, 0, 0) 
screen = pygame.display.set_mode((monitorx, monitory), pygame.FULLSCREEN) 

bilddatei = list((pygame.image.load("dvdvideoblue.png"), pygame.image.load("dvdvideoblueviolet.png"), pygame.image.load("dvdvideocyan.png"), pygame.image.load("dvdvideolachs.png"), pygame.image.load("dvdvideolime.png"),
             pygame.image.load("dvdvideomagenta.png"), pygame.image.load("dvdvideoorange.png"), pygame.image.load("dvdvideopurple.png"), pygame.image.load("dvdvideoseagreen.png"),
             pygame.image.load("dvdvideowhite.png"), pygame.image.load("dvdvideoyellow.png")))
pygame.display.set_caption("DVDVideoScreensaver")

class Symbol:
        _xpos =50
        _ypos =50
        _direction = [2, -2]
        _ymovement = 2
        _xmovement = 2
        _count = 1
        _bild = bilddatei[_count]
        
        def show():
            screen.fill(BLACK)
            screen.blit(Symbol._bild, (Symbol._xpos, Symbol._ypos))
        
        def moveSymbol():
            Symbol._xpos += Symbol._xmovement
            Symbol._ypos += Symbol._ymovement
        
        def checkWalls():
            if Symbol._xpos + 398 >= monitorx:  
                Symbol._xmovement = Symbol._direction[1]
                Symbol._count += 1
            if Symbol._ypos + 260 >= monitory:
                Symbol._ymovement = Symbol._direction[1]
                Symbol._count += 1
            if Symbol._ypos <= 0:
                Symbol._ymovement = Symbol._direction[0]
                Symbol._count += 1
            if Symbol._xpos <= 0:
                Symbol._xmovement = Symbol._direction[0]
                Symbol._count += 1
        
        def matchCount():
            match(Symbol._count):
                case 1:
                    Symbol._bild = bilddatei[1]
                case 2:
                    Symbol._bild = bilddatei[2]
                case 3:
                    Symbol._bild = bilddatei[3]
                case 4:
                    Symbol._bild = bilddatei[4]
                case 5:
                    Symbol._bild = bilddatei[5]
                case 6:
                    Symbol._bild = bilddatei[6]
                case 7:
                    Symbol._bild = bilddatei[7]
                case 8:
                    Symbol._bild = bilddatei[8]
                case 9:
                    Symbol._bild = bilddatei[9]
                case 10:
                    Symbol._bild = bilddatei[10]
                case 11:
                    Symbol._bild = bilddatei[0]
                    Symbol._count -= 10
run = True
while run:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:         
            run = False
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_q:
                run = False
                pygame.quit()               
                sys.exit()
    Symbol.moveSymbol()
    Symbol.checkWalls()
    Symbol.matchCount()
    Symbol.show()
    pygame.display.flip()
    clock.tick(fps)
    
        
