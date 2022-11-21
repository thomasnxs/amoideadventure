import pygame
import random
import os


pygame.init()
resX = 1280
resY = 720
resolucao = (resX, resY)

background = pygame.image.load('assets/background.jpg')
player = pygame.image.load('assets/cj.png')
caneta = pygame.image.load('assets/caneta.png')
caneta = pygame.transform.scale(caneta,(110, 24))
melancia = caneta2 = pygame.image.load('assets/melancia.png')
tela = pygame.display.set_mode(resolucao)
pontos = 4
pygame.display.set_caption('AMOIDE ADVENTURE')

#efeitos sonoros

#musica de fundo
musica_fundo = pygame.mixer.music.load('sounds/feijao.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.07)

#sounds
uh = pygame.mixer.Sound('sounds/uh.mp3')


#posicao dos obj
pos_caneta_x = 1280
pos_caneta_y = 300


pos_player_x = 300
pos_player_y = 200


vel_x_melancia = 0
pos_x_melancia = 300
pos_y_melancia = 200

tiro = False
jogando = True

player_rect = player.get_rect()
caneta_rect = caneta.get_rect()
melancia_rect = melancia.get_rect()

#funcoes (estava dando conflito por isso não criei um arquivo separado para elas)

def respawn():
    x = 1350
    y = random.randint(1, 660)
    return[x, y]

def r():
    tiro = False
    r_x_melancia = pos_player_x
    r_y_melancia = pos_player_y
    vel_x_melancia = 0
    return [r_x_melancia, r_y_melancia, tiro, vel_x_melancia]

def colisao():
    global pontos
    if player_rect.colliderect(caneta_rect): #or caneta_rect.x == 20:
        pontos -=1
        uh.play()
        return True
    elif melancia_rect.colliderect(caneta_rect):
        return True
    else:
        return False

background_user = pygame.image.load("assets/background_user.jpg").convert_alpha()

def name():
    name = ""
    font = pygame.font.Font(None, 32)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    return name
                    break
                else:
                    name += event.unicode
            tela.fill((0, 0, 0))
            tela.blit(background_user, (0, 0))
            block = font.render(name, True, (255, 255, 255))
            rect = block.get_rect()
            rect.center = tela.get_rect().center
            tela.blit(block, rect)
            pygame.display.flip()

if __name__ == "__main__":
    email = name()
    arquivo = open("emails.txt","r")
    emails = arquivo.readlines()
    emails.append(email)
    emails.append("\n")
    arquivo = open("emails.txt","w")
    arquivo.writelines(emails)
    
    arquivo = open("emails.txt","r")
    texto = arquivo.readlines()
    for line in texto:
        print(line)
    arquivo.close()
##

fonte = pygame.font.SysFont('fontes/Minecrafter.Reg.ttf', 50 )

#loop do game
while jogando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    tela.blit(background,(0, 0))
    rel_x = resX % background.get_rect().width
    tela.blit(background, (rel_x - background.get_rect().width,0))#cria background
    if rel_x < 1280:
        tela.blit(background, (rel_x, 0))

    
    #respawn

    if pos_caneta_x == 15:
        pos_caneta_x = respawn()[0]
        pos_caneta_y = respawn()[1]

    if pos_x_melancia == 1280:
        pos_x_melancia, pos_y_melancia, tiro, vel_x_melancia = r()

    if pos_caneta_x == 15 or colisao():
        pos_caneta_x = respawn()[0]
        pos_caneta_y = respawn()[1]
    
    #teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y >-27:
        pos_player_y -=10
        if not tiro:
            pos_y_melancia -=10

    if tecla[pygame.K_DOWN] and pos_player_y < 620:
        pos_player_y +=10
        if not tiro:
            pos_y_melancia +=10

    if tecla[pygame.K_SPACE]:
        tiro = True
        vel_x_melancia = 10

    if pontos == 0:
        
        jogando =  False

        
    #rect
    player_rect.y = pos_player_y
    player_rect.x = pos_player_x

    caneta_rect.y = pos_caneta_y
    caneta_rect.x = pos_caneta_x

    melancia_rect.y = pos_y_melancia
    melancia_rect.x = pos_x_melancia
    #movimento
    resX-=5
    pos_caneta_x -=15    #velocidade da caneta

    pos_x_melancia += vel_x_melancia

    score = fonte.render(f'Vidas: {int(pontos)}', True, (0, 0, 0))
    tela.blit(score,(50, 50))
    

    tela.blit(caneta, (pos_caneta_x, pos_caneta_y))
    tela.blit(melancia, (pos_x_melancia, pos_y_melancia))
    tela.blit(player, (pos_player_x, pos_player_y))
    

    pygame.display.update()
    