class Node:
    def __init__(self):
        self.__leaf = False
        self.__test = None
        self.__children = []

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        pass
        # if isinstance(value, list):
        #     pass
        # else:
        #     raise TypeError

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self, value):
        if isinstance(value, int):
            pass
        else:
            raise TypeError

    @property
    def is_leaf(self):
        return self.__leaf

    @is_leaf.setter
    def is_leaf(self, value):
        if isinstance(value, bool):
            pass
        else:
            raise TypeError
