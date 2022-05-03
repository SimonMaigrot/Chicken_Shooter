import sre_compile
import pygame
import random
from pygame import mixer
from duck import Duck
from shoot import Shoot
pygame.init()
mixer.init()

# Fenêtre jeu
background = pygame.image.load('assets/background.png')
background = pygame.transform.scale(background, (1920, 1080))

# Fenêtre shop
green = pygame.image.load("assets/green.webp")
green = pygame.transform.scale(green, (1920, 1080))

# Taille écran
WIDTH = background.get_width()
HEIGHT = background.get_height()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Variables
duck = Duck(HEIGHT)
duck_1 = Duck(HEIGHT)
shoot = Shoot()

score = 0
life = 3
click = 0

move = True
stat = 'menu'
pause = False

# Texte config.
myfont = pygame.font.SysFont("monospace", 40)

# Texte score
score_text = str(score)
score_display = myfont.render(score_text, 1, (255, 255, 255))
score_string = myfont.render("Score : ", 1, (255, 255, 255))

# Texte vie
life_display = myfont.render(str(life), 1, (255, 255, 255))

# Texte son
son_display = myfont.render(str("ON"), 1, (255, 255, 255))
son_text = myfont.render(str("Son : "), 1, (255, 255, 255))

# Texte difficultée
difficulty_text = myfont.render(str("Difficultée : "), 1, (255, 255, 255))
difficulty = myfont.render(str(int(duck.speed)), 1, (255, 255, 255))

# Images
image_life = pygame.image.load('assets/life_1.png')
image_life = pygame.transform.scale(image_life, (100, 100))

image_menu = pygame.image.load('assets/menu.png')
image_menu = pygame.transform.scale(image_menu, (WIDTH, HEIGHT))

background_menu = pygame.image.load('assets/menu.png')
background_menu = pygame.transform.scale(background_menu, (WIDTH, HEIGHT))

button_play = pygame.image.load('assets/button_play.png')
button_rect = button_play.get_rect()
button_rect.x = 770
button_rect.y = 200

button_option = pygame.image.load("assets/button_option.png")
button_option = pygame.transform.scale(button_option, (390, 120))

option_rect = button_option.get_rect()
option_rect.x = 735
option_rect.y = 400

image_pause = pygame.image.load('assets/pause.png')
image_pause = pygame.transform.scale(image_pause, (170, 170))
pause_rect = image_pause.get_rect()
pause_rect.x = 850
pause_rect.y = 350  

fleche_left = pygame.image.load('assets/fps_gauche.png')
fleche_left = pygame.transform.scale(fleche_left, (120, 120))
fleche_rect_left = fleche_left.get_rect()
fleche_rect_left.x = 720
fleche_rect_left.y = 150

fleche_right = pygame.image.load('assets/fps_droite.png')
fleche_right = pygame.transform.scale(fleche_right, (120, 120))
fleche_rect_right = fleche_right.get_rect()
fleche_rect_right.x = 1000
fleche_rect_right.y = 150

son_left = pygame.image.load('assets/fps_gauche.png')
son_left = pygame.transform.scale(son_left, (120, 120))
son_rect_left = fleche_left.get_rect()
son_rect_left.x = 720
son_rect_left.y = 400

son_right = pygame.image.load('assets/fps_droite.png')
son_right = pygame.transform.scale(son_right, (120, 120))
son_rect_right = fleche_right.get_rect()
son_rect_right.x = 1000
son_rect_right.y = 400

difficulty_left = pygame.image.load('assets/fps_gauche.png')
difficulty_left = pygame.transform.scale(difficulty_left, (120, 120))
difficulty_left_rect = difficulty_left.get_rect()
difficulty_left_rect.x = 720
difficulty_left_rect.y = 650

difficulty_right = pygame.image.load('assets/fps_droite.png')
difficulty_right = pygame.transform.scale(difficulty_right, (120, 120))
difficulty_right_rect = difficulty_left.get_rect()
difficulty_right_rect.x = 1000
difficulty_right_rect.y = 650

duck_or = pygame.image.load("assets/or.png")
duck_or = pygame.transform.scale(duck_or, (290, 215))
duck_or_rect = duck_or.get_rect()
duck_or_rect.x = -100
duck_or_rect.y = random.randint(0, HEIGHT - 100)

def duck_or_move():
    duck_or_rect.x += 6

# Armes
gun = True

sniper_image = pygame.image.load("assets/sniper.png")
sniper_image = pygame.transform.scale(sniper_image, (250, 125))
sniper_rect = sniper_image.get_rect()
sniper_rect.x = 580
sniper_rect.y = 350

sniper = False

ak_image = pygame.image.load("assets/AK-47.png")
ak_image = pygame.transform.scale(ak_image, (275, 85))
ak_rect = ak_image.get_rect()
ak_rect.x = 1100
ak_rect.y = 365

ak = False

# Argent
argent = 1000   

dollar_image = pygame.image.load("assets/dollar.png")
dollar_image = pygame.transform.scale(dollar_image, (123, 123))
dollar_image_rect = dollar_image.get_rect()
dollar_image_rect.x = 1780
dollar_image_rect.y = 925

shop_image = pygame.image.load("assets/shop.png")
shop_image = pygame.transform.scale(shop_image, (180, 180))
shop_rect = shop_image.get_rect()
shop_rect.x = 40
shop_rect.y = 860

price = pygame.image.load("assets/dollar.png")
price = pygame.transform.scale(price, (50, 50))

buy = pygame.image.load("assets/buy.png")
buy = pygame.transform.scale(buy, (100, 60))
buy_rect = buy.get_rect()

price_1 = 300

price_2 = 500

# Son
mixer.music.load("assets/song.ogg")
mixer.music.set_volume(0.9)
mixer.music.play(-1)

# Personnage
character = pygame.image.load("assets/character.png")
character = pygame.transform.scale(character, (500, 504))
character_rect = character.get_rect()
character_rect.x = 10
character_rect.y = 580

# Acheté
ok = pygame.image.load("assets/ok.png")
ok = pygame.transform.scale(ok, (97, 78))
ok_rect = ok.get_rect()

# Musique
music = True

# Fps
clock = pygame.time.Clock()
fps = 60

# Boucle du jeu
running = True
while running:

    # Position souris
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Argent positif
    if argent <= 0:
        argent = 0

    # Apparition souris
    if stat == "game":
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)

    # Stat game
    if stat == "game":

        # Déplacement
        if move:
            duck.move()
            duck_1.move()

        # Respawn
        if duck.rect.x >= WIDTH:
            duck.rect.x = -100
            duck.rect.y = random.randint(0, HEIGHT - 100)
            life = life - 1
            duck.speed = duck.speed + 0.7

        if duck_1.rect.x >= WIDTH:
            duck_1.rect.x = -100
            duck_1.rect.y = random.randint(0, HEIGHT - 100)
            life = life - 1
            duck_1.speed = duck_1.speed + 0.7

        if score == 10 or score == 20 or score == 30 or score == 40 or score == 50:
            duck_or_rect.x = -100
            duck_or_rect.y = random.randint(0, HEIGHT - 100)
            duck_or_move()

        # Vie
        if life == 3:
            image_life = pygame.image.load("assets/life_1.png")

        if life == 2:
            image_life = pygame.image.load('assets/life_2.png')

        if life == 1:
            image_life = pygame.image.load('assets/life_3.png')

        if life == 0:
            stat = "menu"
            life = 3
            duck.speed = 4
            duck_1.speed = 4
            score = 0
            argent -= 50
            duck.rect.x = -100
            duck_1.rect.x = -100
        image_life = pygame.transform.scale(image_life, (100, 100))

    # zoom bouton
    if stat == "menu":
        # Play
        button_play = pygame.image.load("assets/button_play.png")
        if pygame.Rect.collidepoint(button_rect, (mouse_x, mouse_y)):
            button_play = pygame.transform.scale(button_play, (360, 160))
            button_rect.x = 780
            button_rect.y = 190
        else:
            button_play = pygame.transform.scale(button_play, (300, 150))
            button_rect.x = 790
            button_rect.y = 200

        # Option
        button_option = pygame.image.load("assets/button_option.png")
        if pygame.Rect.collidepoint(option_rect, (mouse_x, mouse_y)):
            button_option = pygame.transform.scale(button_option, (360, 160))
            option_rect.x = 790
            option_rect.y = 390
        else:
            button_option = pygame.transform.scale(button_option, (300, 150))
            option_rect.x = 800
            option_rect.y = 400
        
        # Shop
        shop_image = pygame.image.load("assets/shop.png")
        if pygame.Rect.collidepoint(shop_rect, (mouse_x, mouse_y)):
            shop_image = pygame.transform.scale(shop_image, (190, 190))

        else:
            shop_image = pygame.transform.scale(shop_image, (180, 180))

    if stat == "shop":
        sniper_image = pygame.image.load("assets/sniper.png")
        if pygame.Rect.collidepoint(sniper_rect, (mouse_x, mouse_y)):
            sniper_image = pygame.transform.scale(sniper_image, (260, 135))

        else:
            sniper_image = pygame.transform.scale(sniper_image, (250, 125))
        
        ak_image = pygame.image.load("assets/AK-47.png")
        if pygame.Rect.collidepoint(ak_rect, mouse_x, mouse_y):
            ak_image = pygame.transform.scale(ak_image, (285, 95))

        else:
            ak_image = pygame.transform.scale(ak_image, (275, 85))

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
        if stat == "game":

            # Cliquer
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                if pause == False:
                    click += 1
                    if pygame.Rect.collidepoint(duck.rect, mouse_x, mouse_y):
                        score = score + 1
                        duck.rect.x = -100
                        duck.rect.y = random.randint(0, HEIGHT - 100)
                        duck.speed = duck.speed + 0.7
                        if score <= 10:
                            argent += 1
                        if score > 10:
                            argent += 2
                        if score > 15:
                            argent += 4
                        if score > 20:
                            argent += 5
                        if score > 30:
                            argent += 8

                    if pygame.Rect.collidepoint(duck_1.rect, mouse_x, mouse_y):
                        score = score + 1
                        duck_1.rect.x = -100
                        duck_1.rect.y = random.randint(0, HEIGHT - 100)
                        duck_1.speed = duck_1.speed + 0.7
                        if score <= 10:
                            argent += 1
                        if score > 10:
                            argent += 2
                        if score > 15:
                            argent += 4
                        if score > 20:
                            argent += 5
                        if score > 30:
                            argent += 8

                    if pygame.Rect.collidepoint(duck_or_rect, mouse_x, mouse_y):
                        argent = argent + 50

            # Retour et pause
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                stat = "menu"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    move = False
                    pause = True
                    mixer.music.pause()
            
                if event.key == pygame.K_o:
                    move = True
                    pause = False
                    mixer.music.unpause()
                    
        # Boutons            
        if stat == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(button_rect, (mouse_x, mouse_y)):
                    stat = "game"
                if pygame.Rect.collidepoint(option_rect, (mouse_x, mouse_y)):
                    stat = "option"
                if pygame.Rect.collidepoint(shop_rect, mouse_x, mouse_y):
                    stat = "shop"

        if stat == "option":
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Fps
                if pygame.Rect.collidepoint(fleche_rect_left, mouse_x, mouse_y):
                    fps -= 5
                if pygame.Rect.collidepoint(fleche_rect_right, mouse_x, mouse_y):
                    fps += 5
                
                # Son
                if pygame.Rect.collidepoint(son_rect_left, mouse_x, mouse_y):
                    mixer.music.pause()
                    son_display = myfont.render(str("OFF"), 1, (255, 255, 255))
                if pygame.Rect.collidepoint(son_rect_right, mouse_x, mouse_y):
                    mixer.music.unpause()
                    son_display = myfont.render(str("ON"), 1, (255, 255, 255))

                # Difficultée
                if pygame.Rect.collidepoint(difficulty_left_rect, mouse_x, mouse_y):
                    if duck.speed > 1:
                        duck.speed -= 1
                    if duck_1.speed > 1:
                        duck_1.speed -= 1
                if pygame.Rect.collidepoint(difficulty_right_rect, mouse_x, mouse_y):
                    if duck.speed <= 19:
                        duck.speed += 1
                    if duck_1.speed <= 19:
                        duck_1.speed += 1


        # Retour et argent
        if stat == "shop":
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                stat = 'menu'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(sniper_rect, mouse_x, mouse_y):
                    if argent >= 300:
                        argent -= 300
                        sniper = True

                if pygame.Rect.collidepoint(ak_rect, mouse_x, mouse_y):
                    if argent >= 500:
                        argent -= 500
                        ak = True

    # Afichage
    if stat == "game":
        screen.blit(background, (0, 0))
        screen.blit(duck.image, (duck.rect.x, duck.rect.y))
        screen.blit(duck_1.image, (duck_1.rect.x, duck_1.rect.y))


        if pause == False:
            if gun:
                screen.blit(shoot.gun, (mouse_x - 64, mouse_y - 64))

            if sniper == True:
                screen.blit(shoot.sniper, (mouse_x - 150, mouse_y - 150))
                gun = False
                ak = False
            
            if ak == True:
                screen.blit(shoot.ak, (mouse_x - 64, mouse_y - 64))
                gun = False
                sniper = False

            if sniper == True:
                if ak == True:
                   screen.blit(shoot.ak, (mouse_x - 64, mouse_y - 64))
                   gun = False
                   sniper = False

            if ak == True:
                if sniper == True:
                    screen.blit(shoot.sniper, (mouse_x - 150, mouse_y - 150))
                    gun = False
                    ak = False
                
        score_text = str(score)
        score_display = myfont.render(score_text, 1, (255, 255, 255))
        screen.blit(score_string, (10, 10))
        screen.blit(score_display, (190, 12))
        screen.blit(image_life, (1800, 15))
        screen.blit(dollar_image, dollar_image_rect)

        if score == 10:
            screen.blit(duck_or, duck_or_rect)

        argent_display = myfont.render(str(int(argent)), 1, (255, 255, 255))
        screen.blit(argent_display, (1700, 960))

    if stat == "menu":
        screen.blit(background_menu, (0, 0))
        screen.blit(button_play, button_rect)
        screen.blit(button_option, (option_rect.x, option_rect.y))
        screen.blit(shop_image, shop_rect)

    if stat == "option":
        screen.blit(background, (0, 0))
        screen.blit(fleche_left, fleche_rect_left)
        screen.blit(fleche_right, fleche_rect_right)
        screen.blit(son_left, son_rect_left)
        screen.blit(son_right, son_rect_right)

        screen.blit(son_display, (950, 350))
        
        fps_text = myfont.render(str("Fps : "), 1, (255, 255, 255))
        fps_display = myfont.render(str(int(clock.get_fps())), 1, (255, 255,255))

        screen.blit(fps_text, (820, 100))
        screen.blit(fps_display, (950, 100))
        difficulty = myfont.render(str(int(duck.speed)), 1, (255, 255, 255))
        screen.blit(difficulty_text, (650, 580))
        screen.blit(difficulty, (970, 580))
        screen.blit(difficulty_left, difficulty_left_rect)
        screen.blit(difficulty_right, difficulty_right_rect)
        screen.blit(character, character_rect)

        screen.blit(son_text, (800, 350))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            stat = "menu"

    if stat == "shop":        
        # Background
        screen.blit(green, (0, 0))
        # Argent
        argent_display = myfont.render(str(int(argent)), 1, (255, 255, 255))
        screen.blit(dollar_image, (20, 10))
        screen.blit(argent_display, (170, 35))
        # Prix
        price_1_display = myfont.render(str(int(price_1)), 1, (255, 255, 255))
        price_2_display = myfont.render(str(int(price_2)), 1, (255, 255, 255))
        if sniper == False:
            screen.blit(price, (730, 470))
            screen.blit(price_1_display, (630, 475))

        if ak == False:
            screen.blit(price, (1250, 470))
            screen.blit(price_2_display, (1150, 470))

        # Personnage
        screen.blit(character, character_rect)
        # Articles
        screen.blit(sniper_image, sniper_rect)
        screen.blit(ak_image, ak_rect)
        # Achat
        if sniper == True:
            screen.blit(ok, (630, 460))

        if ak == True:
            screen.blit(ok, (1180, 460))

    if move == False:
        screen.blit(image_pause, (pause_rect.x, pause_rect.y))
    

    clock.tick(fps)
    pygame.display.flip()

pygame.quit()