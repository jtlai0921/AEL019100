import logging   # 載入logging套件

logging.basicConfig(level=logging.DEBUG)   # 設定log等級
logger = logging.getLogger('main')   # 產生一個logger物件，同時設定log標籤

num1, num2 = input('請輸入二個介於0和100之間的數字：').split()
num1 = float(num1)
num2 = float(num2)

if num1 < 0 or num1 > 100 or num2 < 0 or num2 > 100:
    print('數字範圍不符合條件')
else:
    logger.debug('數字範圍符合條件：' + str(num1) + ', ' + str(num2))
    average = (num1 + num2) / 2;
    print("二個數字的平均：", average)
