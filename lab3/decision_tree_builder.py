from collections import Counter
from math import log2

from node import Node


def entropy(probabilities: list):
    return - sum([x * log2(x) for x in probabilities])


class DecisionNodeBuilder:
    def __init__(self, decision_table, input_value=None):
        self.__decision_table = decision_table
        self.__input_value = input_value

        self.__attributes = [dict(Counter(x)) for x in zip(*self.__decision_table)]
        self.__probable_values = self.__attributes[-1].keys()
        self.__attributes = self.__attributes[:-1]

    @property
    def decision_table(self):
        return self.__decision_table

    def information(self, attribute_index: int):
        attributes = [dict(Counter(x)) for x in zip(*self.decision_table)]
        all_cases_number = len(self.decision_table)
        information_value = 0
        for key in attributes[attribute_index].keys():
            attribute_cases = [x for x in self.decision_table if x[attribute_index] == key]
            attribute_decision_number = [dict(Counter(x)) for x in zip(*attribute_cases)][-1].values()
            sum_attribute_decision_number = sum(attribute_decision_number)
            information_value += (sum_attribute_decision_number / all_cases_number) * entropy(
                [x / sum_attribute_decision_number for x in attribute_decision_number])

        return information_value

    def decision_class_information(self):
        all_cases_number = len(self.decision_table)
        attributes = [dict(Counter(x)) for x in zip(*self.decision_table)]
        return entropy([x / all_cases_number for x in attributes[-1].values()])

    def gain(self, attribute_index: int):
        return self.decision_class_information() - self.information(attribute_index)

    def split_info(self, attribute_index: int):
        attributes = [dict(Counter(x)) for x in zip(*self.decision_table)]
        all_cases_number = len(self.decision_table)
        return entropy([x / all_cases_number for x in attributes[attribute_index].values()])

    def gain_ratio(self, attribute_index: int):
        split_info = self.split_info(attribute_index)
        if split_info == 0:
            return 0
        else:
            return self.gain(attribute_index) / split_info

    def chose_best_attribute(self):
        best_value = 0
        best_index = 0
        for i in range(len([dict(Counter(x)) for x in zip(*self.decision_table)]) - 1):
            gain_ratio = self.gain_ratio(i)
            if gain_ratio > best_value:
                best_index = i
                best_value = gain_ratio

        return best_index, best_value

    def child_data(self, attribute_index: int):
        data = []
        for key in self.__attributes[attribute_index].keys():
            data.append(tuple(x for x in self.decision_table if x[attribute_index] == key))
        return data

    def build(self):
        node = Node()
        best_attribute = self.chose_best_attribute()
        if best_attribute[1] > 0:
            node.test = best_attribute[0]
            for child_data in self.child_data(best_attribute[0]):
                dnb = DecisionNodeBuilder(child_data, child_data[0][best_attribute[0]])
                node.children.append(dnb.build())
        else:
            node.decision_class = self.__decision_table[0][-1]

        node.input_value = self.__input_value

        return node
