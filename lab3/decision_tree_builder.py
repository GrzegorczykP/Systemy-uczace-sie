from collections import Counter
from math import log2

from node import Node


def entropy(probabilities: list):
    return - sum([x * log2(x) for x in probabilities])


class DecisionTreeBuilder:
    def __init__(self, file_name):
        with open(file_name) as file:
            self.__initial_decision_table = tuple(map(lambda x: tuple(x.strip().split(',')), file))

        attributes = [dict(Counter(x)) for x in zip(*self.__initial_decision_table)]
        self.__probable_values = attributes[-1].keys()

    @property
    def initial_decision_table(self):
        return self.__initial_decision_table

    def information(self, attribute_index: int, decision_table: tuple):
        attributes = [dict(Counter(x)) for x in zip(*decision_table)]
        all_cases_number = len(decision_table)
        information_value = 0
        for key in attributes[attribute_index].keys():
            attribute_cases = [x for x in decision_table if x[attribute_index] == key]
            attribute_decision_number = [dict(Counter(x)) for x in zip(*attribute_cases)][-1].values()
            sum_attribute_decision_number = sum(attribute_decision_number)
            information_value += (sum_attribute_decision_number / all_cases_number) * entropy(
                [x / sum_attribute_decision_number for x in attribute_decision_number])

        return information_value

    def decision_class_information(self, decision_table: tuple):
        all_cases_number = len(decision_table)
        attributes = [dict(Counter(x)) for x in zip(*decision_table)]
        return entropy([x / all_cases_number for x in attributes[-1].values()])

    def gain(self, attribute_index: int, decision_table: tuple):
        return self.decision_class_information(decision_table) - self.information(attribute_index, decision_table)

    def split_info(self, attribute_index: int, decision_table: tuple):
        attributes = [dict(Counter(x)) for x in zip(*decision_table)]
        all_cases_number = len(decision_table)
        return entropy([x / all_cases_number for x in attributes[attribute_index].values()])

    def gain_ratio(self, attribute_index: int, decision_table: tuple):
        split_info = self.split_info(attribute_index, decision_table)
        if split_info == 0:
            return 0
        else:
            return self.gain(attribute_index, decision_table) / split_info

    def chose_best_attribute(self, decision_table: tuple):
        best_value = 0
        best_index = 0
        for i in range(len([dict(Counter(x)) for x in zip(*decision_table)])):
            gain_info = self.gain_ratio(i, decision_table)
            if gain_info > best_value:
                best_index = i
                best_value = gain_info

        return best_index, best_value

    def child_data(self, attribute_index: int, decision_table: tuple):
        attributes = [dict(Counter(x)) for x in zip(*decision_table)]
        data = []
        for key in attributes[attribute_index].keys():
            data.append(tuple(x for x in decision_table if x[attribute_index] == key))
        return data

    def build(self, decision_table):
        node = Node()
        best_attribute = self.chose_best_attribute(decision_table)
        if best_attribute[1] > 0:
            node.test = best_attribute[0]
            for child_data in self.child_data(best_attribute[0], decision_table):
                node.children.append(self.build(child_data))
        else:
            node.is_leaf = True

        return node
