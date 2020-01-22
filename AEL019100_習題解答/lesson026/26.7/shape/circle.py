# 載入math套件，我們要用它的圓周率pi值
import math


class Circle:
    # 建構式的第二個參數是用來接收傳入的半徑
    def __init__(self, radius):
        # 利用self參數建立類別內部專用的變數
        # 把半徑存入這個變數
        self._radius = radius

    # 這個方法用來取得半徑
    def get_radius(self):
        return self._radius  # 傳回類別內部變數的值

    # 這個方法用來設定半徑，第二個參數用來傳入半徑
    def set_radius(self, radius):
        self._radius = radius  # 把半徑存入類別內部的變數

    # 這個方法用來取得圓面積
    def get_area(self):
        # 利用類別內部的變數計算圓面積，然後傳回結果
        return math.pi * self._radius * self._radius

    # 這個方法用來取得圓周長度
    def get_perimeter(self):
        # 利用類別內部的變數計算圓周長度，然後傳回結果
        return 2 * math.pi * self._radius
