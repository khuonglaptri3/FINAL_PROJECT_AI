import pygame
from time import sleep
from random import randint

 

pygame.init()
screen = pygame.display.set_mode((501, 601))
pygame.display.set_caption('Snake')
running = True
GREEN = (140, 194, 75)
BLACK = (0,0,0)
WHITE = (255,255,255)
BG_COLOR = (24, 46, 48)
BLUE = (50, 153, 213)

 


# Snake position
# tail - head
snakes = [[3, 10], [4, 10], [5, 10]]
direction = "right"



head_r = pygame.transform.scale(pygame.image.load('snake_finally/snake_head-1.png'), (20, 20))
head_l = pygame.transform.scale(pygame.image.load('snake_finally/snake_head-2.png'), (20, 20))
head_u = pygame.transform.scale(pygame.image.load('snake_finally/snake_head-3.png'), (20, 20))
head_d = pygame.transform.scale(pygame.image.load('snake_finally/snake_head-4.png'), (20, 20))

apple_r = pygame.transform.scale(pygame.image.load('snake_finally/apple.png'), (20, 20))
apple_g = pygame.transform.scale(pygame.image.load('snake_finally/green_apple.png'), (20, 20))

apple_rb = pygame.transform.scale(pygame.image.load('snake_finally/apple.png'), (40, 40))
apple_gb = pygame.transform.scale(pygame.image.load('snake_finally/green_apple.png'), (40, 40))

apple = [randint(1, 24), randint(1, 24)]
apple_green = [randint(4, 22), randint(4, 22)]
font_small = pygame.font.SysFont('Comic Sans MS', 25)
font_big = pygame.font.SysFont('Comic Sans MS', 40)
score = 0

score_down = 50
bonus = 0

level = 1
pausing = False

frame_img = pygame.transform.scale(pygame.image.load('snake_finally/frame.png'), (500, 100))
game_over_img = pygame.transform.scale(pygame.image.load('snake_finally/gameover.png'), (300, 65))

while running:        
    screen.fill(BG_COLOR)

    # for i in range(26):
    #     pygame.draw.line(screen, WHITE,(0,i*20),(500,i*20))
    #     pygame.draw.line(screen, WHITE,(i*20,0),(i*20,500))

 

    # Draw snake
    for snake in snakes:
        pygame.draw.rect(screen, GREEN, (snake[0]*20, snake[1]*20, 20, 20))

 

    # Draw apple
    screen.blit(apple_r, (apple[0]*20, apple[1]*20))
    if score % 5 == 0 and score != 0:
        screen.blit(apple_g, (apple[0]*20, apple[1]*20))
 

    tail_x = snakes[0][0]
    tail_y = snakes[0][1]
    # point
    if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
        snakes.insert(0,[tail_x,tail_y])
        apple = [randint(0,19), randint(0,19)]
        score += 1

    if snakes[-1][0] == apple_green[0] and snakes[-1][1] == apple_green[1]:
        snakes.insert(0,[tail_x,tail_y])
        apple_green = [randint(4, 22), randint(4, 22)]
        score_down -= 5
        bonus += score_down

    # # check crash with edge
    # if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
    #     pausing = True
    #xuyên map
    if snakes[-1][0] < 0:
        snakes.append([snakes[-1][0]+25, snakes[-1][1]])
        snakes.pop(0)
    if snakes[-1][0] > 24:
        snakes.append([snakes[-1][0]-25, snakes[-1][1]])
        snakes.pop(0)
    if snakes[-1][1] < 0:
        snakes.append([snakes[-1][0], snakes[-1][1] +25])
        snakes.pop(0)
    if snakes[-1][1] > 24:
        snakes.append([snakes[-1][0], snakes[-1][1] -25])
        snakes.pop(0)
 

    # Draw score
    screen.blit(frame_img, (0, 500))
    screen.blit(apple_rb, (50, 525))
    score_txt = font_small.render("x" + str(score), True, WHITE)
    screen.blit(score_txt, (90, 530))


    screen.blit(apple_gb, (330, 525))
    bonus_txt = font_small.render("x" + str(bonus), True, GREEN)
    screen.blit(bonus_txt, (370, 530))

 

    # Snake move
    if pausing == False:
        if direction == "right":
            head = screen.blit(head_r, (snakes[-1][0]*20, snakes[-1][1]*20))
            snakes.append([snakes[-1][0]+1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "left":
            head = screen.blit(head_l, (snakes[-1][0]*20, snakes[-1][1]*20))
            snakes.append([snakes[-1][0]-1, snakes[-1][1]])
            snakes.pop(0)
        if direction == "up":
            head = screen.blit(head_u, (snakes[-1][0]*20, snakes[-1][1]*20))
            snakes.append([snakes[-1][0], snakes[-1][1]-1])
            snakes.pop(0)
        if direction == "down":
            head = screen.blit(head_d, (snakes[-1][0]*20, snakes[-1][1]*20))
            snakes.append([snakes[-1][0], snakes[-1][1]+1])
            snakes.pop(0)
    
    # check crash with body
    for i in range(len(snakes)-1):
        if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1]:
            pausing = True

 

    # Draw game over
    if pausing:

        screen.blit(game_over_img, (100, 200))
        press_space_txt = font_big.render("Press Space to continue", True, WHITE)

        screen.blit(apple_rb, (180, 300))
        score_txt = font_small.render("x" + str(score), True, WHITE)
        screen.blit(score_txt, (230, 305))
        screen.blit(press_space_txt, (50,300))

        screen.blit(apple_gb, (180, 355))
        bonus_txt = font_small.render("x" + str(bonus), True, GREEN)
        screen.blit(bonus_txt, (230, 360))
        total_txt = font_big.render("Total: " +str(bonus + score), True, GREEN)
        screen.blit(total_txt, (160, 400))
 

    sleep(0.1)

 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            if event.key == pygame.K_SPACE and pausing == True:
                pausing = False
                snakes = [[5,10]]
                apple = [randint(0,19), randint(0,19)]
                score = 0

 

    pygame.display.flip()

 

pygame.quit()