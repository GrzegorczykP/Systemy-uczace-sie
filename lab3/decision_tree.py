from decision_tree_builder import DecisionNodeBuilder


class DecisionTree:
    def __init__(self, file_name):
        with open(file_name) as file:
            decision_table = tuple(map(lambda x: tuple(x.strip().split(',')), file))
        dnb = DecisionNodeBuilder(decision_table)
        self.__root = dnb.build()

    def __str__(self):
        return str(self.__root)
