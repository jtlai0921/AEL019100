class Rect:
    # 建構式的第二個和第三個參數是用來接收矩形的長和寬
    def __init__(self, length, width):
        self._length = length
        self._width = width

    # 這個方法用來取得矩形面積
    def get_area(self):
        return self._length * self._width

    # 這個方法用來取得矩形周長
    def get_perimeter(self):
        return 2 * (self._length + self._width)
