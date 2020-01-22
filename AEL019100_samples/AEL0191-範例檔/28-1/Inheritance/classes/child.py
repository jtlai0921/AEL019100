from classes.parent import *

class Child(Parent):
    def __init__(self):
        super().__init__()

    # 這個方法會用到從父類別得到的公開變數public_var
    def get_super_public_var(self):
        return self.public_var

    # 這個方法會用到從父類別得到的保護變數protected_var
    def get_super_protected_var(self):
        return self._protected_var

    # 這個方法會用到從父類別得到的私有變數private_var
    def get_super_private_var(self):
        return self.__private_var

    # 這個方法會用到從父類別得到的公開方法public_method()
    def call_super_public_method(self):
        return self.public_method()

    # 這個方法會用到從父類別得到的保護方法protected_method()
    def call_super_protected_method(self):
        return self._protected_method()

    # 這個方法會用到從父類別得到的私有方法private_method()
    def call_super_private_method(self):
        return self.__private_method()
