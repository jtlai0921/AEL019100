class Square:
    def __init__(self, size):
        self.__size = size

    def show_shape_info(self):
        print('正方形，邊長' + str(self.__size))

    def get_area(self):
        return self.__size * self.__size
