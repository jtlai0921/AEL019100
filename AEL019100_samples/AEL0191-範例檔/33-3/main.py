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

# 這個函式負責刪除超出畫面範圍以外的圖案
def check_and_remove():
    # 檢查是否超出畫面範圍
    remove = []
    for i in range(len(falling)):
        if falling[i][2] > height:
            remove += [i]   # 記下超出範圍的圖案索引值

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

# 這個資料組用來記錄畫面中所有圖案
falling = []

# 用來計算二次畫面更新之間的時間差，藉此決定移動的距離
last_screen_update = None
last_produce = None   # 用來判斷是否要加入新圖案

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

        # 記錄最後一次更新畫面的時間
        last_screen_update = now

    # 更新遊戲畫面
    pg.display.flip()

    # 呼叫函式移除超出畫面範圍的圖案
    check_and_remove()

    # 取得使用者的操作並加以處理
    for event in pg.event.get():
        if event.type == pg.QUIT:   # 表示要關閉遊戲程式
            pg.quit()
            exit
