class Parent:
    def __init__(self):
        self.public_var = 'Parent類別的公開變數'
        self._protected_var = 'Parent類別的保護變數'
        self.__private_var = 'Parent類別的私有變數'

    def public_method(self):
        return 'Parent類別的公開方法'

    def _protected_method(self):
        return 'Parent類別的保護方法'

    def __private_method(self):
        return 'Parent類別的私有方法'
