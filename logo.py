import pygame
import sys
import random
import math

pygame.init()
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("logo")

clock = pygame.time.Clock()

# 顏色
black = (0, 0, 0)
white = (255, 255, 255)

# 中心位置
cx, cy = 225, 225


# 十字數量
num_cross = 50

# 十字範圍
r_inner = 100
r_outer = 200

# 十字大小設定
cross_base_length = 7  # 基礎長度
cross_width = 2        # 線寬
cross_size_variation = 2  # 最大隨機變化 +/- 像素

# 隨機座標
def random_point_in_ring(cx, cy, r_inner, r_outer):
    r = random.uniform(r_inner, r_outer)
    theta = random.uniform(0, 2 * math.pi)
    x = cx + r * math.cos(theta)
    y = cy + r * math.sin(theta)
    return x, y

# 畫出十字
def draw_cross(surface, color, center, length=cross_base_length, width=cross_width):
    x, y = center
    half = length / 2
    pygame.draw.line(surface, color, (x, y - half), (x, y + half), width)  # 垂直
    pygame.draw.line(surface, color, (x - half, y), (x + half, y), width)  # 水平

# 初始化十字座標
crosses = [random_point_in_ring(cx, cy, r_inner, r_outer) for _ in range(num_cross)]

# 刷新十字位置計時器
update_crosses_event = pygame.USEREVENT + 1
pygame.time.set_timer(update_crosses_event, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == update_crosses_event:
            crosses = [random_point_in_ring(cx, cy, r_inner, r_outer) for _ in range(num_cross)]

    screen.fill(black)

    # logo主體中心區域
    pygame.draw.circle(screen, white, (cx, cy), 20, 4)
    pygame.draw.line(screen, white, (225, 245), (225, 285), 3)
    pygame.draw.line(screen, white, (225, 205), (225, 165), 3)
    pygame.draw.line(screen, white, (245, 225), (285, 225), 3)
    pygame.draw.line(screen, white, (205, 225), (165, 225), 3)
    pygame.draw.line(screen, white, (239, 239), (255, 255), 4)
    pygame.draw.line(screen, white, (211, 211), (195, 195), 4)
    pygame.draw.line(screen, white, (239, 211), (255, 195), 4)
    pygame.draw.line(screen, white, (211, 239), (195, 255), 4)

    # 外圈第一層
    pygame.draw.circle(screen, white, (cx, cy), 85, 4)
    pygame.draw.rect(screen, black, [205, 140, 40, 10])
    pygame.draw.rect(screen, black, [205, 300, 40, 10])
    pygame.draw.rect(screen, black, [140, 205, 10, 40])
    pygame.draw.rect(screen, black, [300, 205, 10, 40])
    # 外圍三角形
    triangle_1 = [(225, 130), (215, 150), (235, 150)]
    triangle_2 = [(130, 225), (150, 235), (150, 215)]
    triangle_3 = [(320, 225), (300, 235), (300, 215)]
    triangle_4 = [(225, 320), (215, 300), (235, 300)]
    pygame.draw.lines(screen, white, True, triangle_1, 3)
    pygame.draw.lines(screen, white, True, triangle_2, 3)
    pygame.draw.lines(screen, white, True, triangle_3, 3)
    pygame.draw.lines(screen, white, True, triangle_4, 3)
    # 外圍圓點裝飾
    pygame.draw.circle(screen, white, (285.1, 285.1), 9)
    pygame.draw.circle(screen, white, (164.9, 285.1), 9)
    pygame.draw.circle(screen, white, (164.9, 164.9), 9)
    pygame.draw.circle(screen, white, (285.1, 164.9), 9)
    # 挖空
    pygame.draw.circle(screen, black, (285.1, 285.1), 5)
    pygame.draw.circle(screen, black, (164.9, 285.1), 5)
    pygame.draw.circle(screen, black, (164.9, 164.9), 5)
    pygame.draw.circle(screen, black, (285.1, 164.9), 5)


    
    for pos in crosses:
        length = cross_base_length + random.uniform(-cross_size_variation, cross_size_variation)
        draw_cross(screen, white, pos, length=length, width=cross_width)

    pygame.display.flip()
    clock.tick(60)
