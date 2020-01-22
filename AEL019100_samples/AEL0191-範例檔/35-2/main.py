import pygame as pg   # 載入PyGame套件
import datetime as dt   # 用來計算時間差
import random   # 亂數

# 這個函式用來產生一個新圖案
def produce():
    # 決定x座標
    x = random.randint(0, width - python_icon.get_width())

    # 決定移動的速度
    y_step = random.randint(20, 100)

    # 把新圖案加入資料組
    global falling
    falling += [[python_icon, x, 0, y_step]]

# 這個函式負責執行碰撞檢測和刪除超出畫面範圍以外的圖案
def check_and_remove():
    remove = []

    # 取得bar的最小外接矩形
    bar_rect = bar.get_rect()
    bar_rect.left = bar_pos[0]
    bar_rect.top = bar_pos[1]

    for i in range(len(falling)):
        # 取得Python圖案的最小外接矩形
        rect = falling[i][0].get_rect()
        rect.left = falling[i][1]
        rect.top = falling[i][2]

        # 碰撞偵測
        if rect.colliderect(bar_rect):
            remove += [i]

            # 加一分
            global score
            score += 1

            sound_catch.play()   # 播放音效
        elif rect.top > height:   # Python圖案超出畫面範圍
            remove += [i]
            sound_disappear.play()   # 播放音效

    # 必須從最後往前刪除，才能維持索引的正確
    for i in remove[::-1]:
        falling.pop(i)

# PyGame初始化
pg.init()
width, height = 640, 480   # 遊戲畫面的寬和高
screen = pg.display.set_mode((width, height))
pg.display.set_caption('PyGame遊戲程式')   # 設定程式標題

# 載入圖檔，然後縮小到50x50
python_icon = pg.image.load('resources\\images\\python.png')
python_icon = pg.transform.scale(python_icon, (50, 50))
bar = pg.image.load('resources\\images\\bar.png')

# 這個資料組用來記錄畫面中所有圖案
falling = []

# 設定bar的位置和左右方向鍵的狀態
bar_pos = [int(((width - bar.get_width()) / 2)), 400]
key_left_right = [False, False]   # 記錄按鍵的狀態

# 用來計算二次畫面更新之間的時間差，藉此決定移動的距離
last_screen_update = None
last_produce = None   # 用來判斷是否要加入新圖案

# 準備音效
pg.mixer.init()   # 音效功能初始化
sound_catch = pg.mixer.Sound('resources\\audio\\catch.wav')
sound_disappear = pg.mixer.Sound('resources\\audio\\disappear.wav')
sound_catch.set_volume(1)
sound_disappear.set_volume(1)
pg.mixer.music.load('resources\\audio\\bg_music.wav')   # 遊戲背景音樂
pg.mixer.music.set_volume(0.25)
pg.mixer.music.play(-1)   # 重複播放

#  設定中文字型
font = pg.font.SysFont('mingliupmingliumingliuhkscs', 16)

# 累計得分
score = 0

# 遊戲開始時間
time_start = dt.datetime.now()

# 利用迴圈更新遊戲畫面，並且取得使用者的操作然後加以處理
while True:
    # 將遊戲畫面填入指定的底色
    screen.fill((255, 255, 255))

    now = dt.datetime.now()

    if not last_screen_update:   # 表示是第一個畫面
        last_screen_update = now
        last_produce = now
        produce()   # 呼叫產生新圖案的函式
    else:   # 第二個畫面以後
        time_diff = now - last_screen_update

        # 根據時間差，更新所有圖案的y座標
        for i in range(len(falling)):
            falling[i][2] += falling[i][3] * time_diff.total_seconds()

        # 顯示全部圖案
        for item in falling:
            screen.blit(item[0], (item[1], item[2]))

        # 計算時間差，決定是否產生一個新圖案
        if (now - last_produce).total_seconds() >= 1:
            last_produce = now
            produce()   # 呼叫產生新圖案的函式

        # 根據左右方向鍵的狀態移動bar的位置
        if key_left_right[0]:   # 往左
            bar_pos[0] -= time_diff.total_seconds() * 200
        elif key_left_right[1]: # 往右
            bar_pos[0] += time_diff.total_seconds() * 200

        screen.blit(bar, bar_pos)

        # 記錄最後一次更新畫面的時間
        last_screen_update = now

    # 顯示遊戲時間和分數
    time_from_start = now - time_start   # 計算遊戲時間
    text_time = font.render('遊戲時間: ' +
            str(time_from_start.seconds) + '秒', True, (0, 0, 255))
    screen.blit(text_time, (500, 10))
    text_score = font.render('得    分: ' +
            str(score), True, (0, 0, 255))
    screen.blit(text_score, (500, 30))

    # 更新遊戲畫面
    pg.display.flip()

    # 呼叫函式移除超出畫面範圍的圖案
    check_and_remove()

    # 取得使用者的操作並加以處理
    for event in pg.event.get():
        if event.type == pg.QUIT:   # 表示要關閉遊戲程式
            pg.mixer.music.stop()
            pg.quit()
            exit
        elif event.type == pg.KEYDOWN:   # 檢查左右方向鍵是否被按下
            if event.key == pg.K_LEFT:
                key_left_right[0] = True
            elif event.key == pg.K_RIGHT:
                key_left_right[1] = True
        elif event.type == pg.KEYUP:   # 檢查左右方向鍵是否被放開
            if event.key == pg.K_LEFT:
                key_left_right[0] = False
            elif event.key == pg.K_RIGHT:
                key_left_right[1] = False
