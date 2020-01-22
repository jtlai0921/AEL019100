import pygame as pg   # 載入PyGame套件
import datetime as dt   # 用來計算時間差

# PyGame初始化
pg.init()
width, height = 640, 480   # 遊戲畫面的寬和高
screen = pg.display.set_mode((width, height))
pg.display.set_caption('PyGame遊戲程式')   # 設定程式標題

# 載入圖檔
python_icon = pg.image.load('resources\\images\\python.png')

# 圖片的初始位置在畫面中央
pos = [(width - python_icon.get_width()) / 2,
       (height - python_icon.get_height()) / 2]

# 用來記錄方向鍵是否被按下
key_pressed = [False, False, False, False]   # 上、下、左、右

# 用來計算二次畫面更新之間的時間差，藉此決定圖片移動的距離
last_screen_update = None
steps_per_sec = 80   # 每秒移動的距離（像素）

# 利用迴圈更新遊戲畫面，並且取得使用者的操作然後加以處理
while True:
    # 將遊戲畫面填入指定的底色
    screen.fill((255, 255, 255))

    # 設定圖檔和顯示的位置
    screen.blit(python_icon, pos)

    # 更新遊戲畫面
    pg.display.flip()

    # 取得使用者的操作並加以處理
    for event in pg.event.get():
        if event.type == pg.QUIT:   # 表示要關閉遊戲程式
            pg.quit()
            exit
        elif event.type == pg.KEYDOWN:   # 表示有按鍵被按下
            # 檢查是否是方向鍵
            if event.key == pg.K_UP:
                key_pressed[0] = True
            elif event.key == pg.K_DOWN:
                key_pressed[1] = True
            elif event.key == pg.K_LEFT:
                key_pressed[2] = True
            elif event.key == pg.K_RIGHT:
                key_pressed[3] = True
        elif event.type == pg.KEYUP:   # 表示有按鍵被放開
            # 檢查是否是方向鍵
            if event.key == pg.K_UP:
                key_pressed[0] = False
            elif event.key == pg.K_DOWN:
                key_pressed[1] = False
            elif event.key == pg.K_LEFT:
                key_pressed[2] = False
            elif event.key == pg.K_RIGHT:
                key_pressed[3] = False

    now = dt.datetime.now()

    if not last_screen_update:   # 表示是第一個畫面
        last_screen_update = now
    else:
        # 根據方向鍵的狀態，以及畫面更新的時間差
        # 決定圖片移動的距離
        time_diff = now - last_screen_update

        if key_pressed[0]:   # 上
            pos[1] -= steps_per_sec * time_diff.total_seconds()
        if key_pressed[1]:   # 下
            pos[1] += steps_per_sec * time_diff.total_seconds()
        if key_pressed[2]:   # 左
            pos[0] -= steps_per_sec * time_diff.total_seconds()
        if key_pressed[3]:   # 右
            pos[0] += steps_per_sec * time_diff.total_seconds()

        # 記錄最後一次更新畫面的時間
        last_screen_update = now
