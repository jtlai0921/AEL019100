try:
    a = 5
    len(a)

    a = [1, 2, 3]
    b = {1, 2, 4}
    c = a & b
except TypeError:
    print("len()只能夠處理資料組。")
    print("集合運算子只能夠用在集合資料組。")
