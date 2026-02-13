import pygame
import random
import math

pygame.init()

# 設定視窗寬度和高度
WIDTH, HEIGHT = 768, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")

# 設定遊戲時鐘
clock = pygame.time.Clock()

# 定義顏色
BLACK = (0, 0, 0)
BLUE = (50, 100, 200)
YELLOW = (255, 220, 0)
RED = (200, 50, 50)
WHITE = (255, 255, 255)

# 球的半徑
radius = 70

# 球A和球B的初始位置
x1 = random.randint(radius, WIDTH // 2 - radius*2)
y1 = random.randint(radius, HEIGHT - radius)
x2 = random.randint(WIDTH // 2 + radius*2, WIDTH - radius)
y2 = random.randint(radius, HEIGHT - radius)

# 初始繪製球
pygame.draw.circle(screen, RED, (x1,y1), 20, 0)
pygame.draw.circle(screen, BLUE, (x2,y2), 20, 0)

# 初始速度向量（x軸和y軸分量）
i1 = random.uniform(4,6)
j1 = random.uniform(4,6)
i2 = random.uniform(1,3)
j2 = random.uniform(1,3)

# 球的顏色初值
color_A = (255,0,0)
color_B = (0,0,255)

# 主遊戲迴圈
while True:
    # 填充背景顏色
    screen.fill((255,217,170))

    # 處理事件
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    # 球A的移動和繪製
    pygame.draw.circle(screen, color_A, (int(x1), int(y1)), radius)
    x1 += i1
    y1 += j1

    # 球A與牆壁的碰撞檢測
    if x1 - radius <= 0 or x1 + radius >= WIDTH:
        i1 *= -1
    if y1 - radius <= 0 or y1 + radius >= HEIGHT:
        j1 *= -1

    # 球B的移動和繪製
    pygame.draw.circle(screen, color_B, (int(x2), int(y2)), radius)
    x2 += i2
    y2 += j2

    # 球B與牆壁的碰撞檢測
    if x2 - radius <= 0 or x2 + radius >= WIDTH:
        i2 *= -1
    if y2 - radius <= 0 or y2 + radius >= HEIGHT:
        j2 *= -1

    # 球A和球B的碰撞檢測與處理
    dist = math.hypot(x2 - x1, y2 - y1)
    # 當球相碰時交換速度並變色
    if dist <= radius * 2:
        # 交換x軸速度
        i1, i2 = i2, i1
        # 交換y軸速度
        j1, j2 = j2, j1
        # 隨機變更球A的顏色
        color_A = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # 隨機變更球B的顏色
        color_B = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    # 更新顯示並設定幀率為每秒120幀
    pygame.display.flip()
    clock.tick(120)
