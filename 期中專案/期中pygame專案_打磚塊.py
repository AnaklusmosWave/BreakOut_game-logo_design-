import pygame
import random
import os

#--------------------------

clock = pygame.time.Clock()

def random_color():
    return (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))

#--------------------------

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#--------------------------

screen_width = 800
screen_height = 600

#--------------------------

all = pygame.sprite.Group()
board_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

#--------------------------
 
class Board(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (screen_width - self.rect.width) // 2
        self.rect.y = screen_height - 25
        self.speed = 20

    def update(self):
        if key_pressed[pygame.K_RIGHT]:
            if self.rect.right<800:
                self.rect.x += self.speed
            else:
                self.rect.right=800
        if key_pressed[pygame.K_LEFT]:
            if self.rect.left>0:
                self.rect.x -= self.speed
            else:
                self.rect.left=0

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, block_width, block_height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((block_width, block_height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

    def godown(self):
        self.rect.y += self.rect.height + block_space_y

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((WHITE))
        
        player_img = pygame.image.load(os.path.join(os.path.dirname(__file__), "ball.jpg")).convert()
        self.image = pygame.transform.scale(player_img ,(20,20))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.centery = screen_height - 75
        self.speedx = 6
        self.speedy = 6
        
    def update(self):
        
        self.last_left = self.rect.left
        self.last_right = self.rect.right
        self.last_top = self.rect.top
        self.last_bottom = self.rect.bottom

        if self.rect.right >= screen_width:
            self.rect.right = screen_width
            self.speedx *= -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.speedx *= -1
        elif self.rect.top <= 0:
            self.rect.top = 0
            self.speedy *= -1
        elif self.rect.bottom >= screen_height:
            global running
            running = False

        self.rect.centerx += self.speedx
        self.rect.centery += self.speedy

#--------------------------

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("期中專題:打磚塊")

#--------------------------

board = Board()
all.add(board)
board_group.add(board)

ball = Ball()
all.add(ball)
ball_group.add(ball)

side_block_space = 20
top_block_space = 20

block_space_x = 10
block_space_y = 10

min_block_width = 30
max_block_width = 100

block_height = 45

def create_row(y):
    x = side_block_space
    remain_space = screen_width - 2 * side_block_space

    while remain_space >= min_block_width:
        w = random.randint(min_block_width, min(max_block_width, remain_space))
        remain_space_after = remain_space - (w + block_space_x)
        
        if 0 < remain_space_after < min_block_width:
            w += remain_space_after

        block = Block(x, y, w, block_height, random_color())
        all.add(block)
        block_group.add(block)

        x += w + block_space_x
        remain_space -= (w + block_space_x)

#--------------------------

running = True

while running:

    clock.tick(60)
    screen.fill(BLACK)
    key_pressed = pygame.key.get_pressed()

    for e in pygame.event.get():

        if e.type == pygame.QUIT or key_pressed[pygame.K_ESCAPE]:
            running = False

    if len(block_group) < 40:
        for block in list(block_group):
            block.godown()

        create_row(top_block_space)

    all.update()

    d1 = pygame.sprite.groupcollide(ball_group,block_group,False,True)
    for ball, blocks in d1.items():
        for block in blocks:

            # 上側撞擊
            if ball.last_bottom <= block.rect.top and ball.rect.bottom >= block.rect.top:
                ball.rect.bottom = block.rect.top
                ball.speedy *= -1
            # 左側撞擊
            elif ball.last_right <= block.rect.left and ball.rect.right >= block.rect.left:
                ball.rect.right = block.rect.left
                ball.speedx *= -1
            # 右側撞擊
            elif ball.last_left >= block.rect.right and ball.rect.left <= block.rect.right:
                ball.rect.left = block.rect.right
                ball.speedx *= -1
            # 下側撞擊
            elif ball.last_top >= block.rect.bottom and ball.rect.top <= block.rect.bottom:
                ball.rect.top = block.rect.bottom
                ball.speedy *= -1

    d2 = pygame.sprite.groupcollide(ball_group, board_group, False, False)
    for ball, paddles in d2.items():
        if ball:
            ball.speedy *= -1
            ball.rect.bottom = screen_height - 25

    all.draw(screen)

    pygame.display.update()

pygame.quit()


