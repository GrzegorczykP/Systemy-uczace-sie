from decision_tree_builder import DecisionTreeBuilder


class DecisionTree:
    def __init__(self, file_name):
        dtb = DecisionTreeBuilder(file_name)
        self.__root = dtb.build(dtb.initial_decision_table)

    def __str__(self):
        return self.__root
