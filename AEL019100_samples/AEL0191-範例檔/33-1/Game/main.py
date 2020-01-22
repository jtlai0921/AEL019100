# 載入PyGame套件
import pygame as pg

# PyGame初始化
pg.init()
width, height = 640, 480   # 遊戲畫面的寬和高
screen = pg.display.set_mode((width, height))
pg.display.set_caption('PyGame遊戲程式')   # 設定程式標題

# 載入圖檔
python_icon = pg.image.load('resources\\images\\python.png')

# 計算圖片顯示的位置，包括畫面中央，以及上下左右
# 圖片的位置是根據遊戲畫面的寬和高，以及圖片的寬和高來計算
pos1 = [(width - python_icon.get_width()) * 1 / 4,
       (height - python_icon.get_height()) / 2]
pos2 = [(width - python_icon.get_width()) / 2,
       (height - python_icon.get_height()) / 2]
pos3 = [(width - python_icon.get_width()) * 3 / 4,
       (height - python_icon.get_height()) / 2]
pos4 = [(width - python_icon.get_width()) / 2,
       (height - python_icon.get_height()) * 1 / 4]
pos5 = [(width - python_icon.get_width()) / 2,
       (height - python_icon.get_height()) * 3 / 4]

# 利用迴圈更新遊戲畫面，並且取得使用者的操作然後加以處理
while True:
    # 將遊戲畫面填入指定的底色
    screen.fill((255, 255, 255))

    # 設定圖檔和顯示的位置
    screen.blit(python_icon, pos1)
    screen.blit(python_icon, pos2)
    screen.blit(python_icon, pos3)
    screen.blit(python_icon, pos4)
    screen.blit(python_icon, pos5)

    # 更新遊戲畫面
    pg.display.flip()

    # 取得使用者的操作並加以處理
    for event in pg.event.get():
        if event.type == pg.QUIT:   # 表示要關閉遊戲程式
            pg.quit()
            exit
