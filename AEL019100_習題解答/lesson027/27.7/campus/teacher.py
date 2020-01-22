class Teacher:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_data(self):
        return self._name, self._age