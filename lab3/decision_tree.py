from collections import Counter
from math import log2


def entropy(probabilities: list):
    return - sum([x * log2(x) for x in probabilities])


class DecisionTree:
    def __init__(self, file_name):
        with open(file_name) as file:
            self.__decision_table = list(map(lambda x: x.strip().split(','), file))

        self.__attributes = [dict(Counter(x)) for x in zip(*self.__decision_table)]
        self.__probable_values = self.__attributes[-1].keys()
        self.__attributes = self.__attributes[:-1]

    @property
    def decision_table(self):
        return self.__decision_table

    def information(self, attribute_index: int):
        attributes = [dict(Counter(x)) for x in zip(*self.__decision_table)]
        all_cases_number = len(self.__decision_table)
        information_value = 0
        for key in attributes[attribute_index].keys():
            attribute_cases = [x for x in self.__decision_table if x[attribute_index] == key]
            attribute_decision_number = [dict(Counter(x)) for x in zip(*attribute_cases)][-1].values()
            sum_attribute_decision_number = sum(attribute_decision_number)
            information_value += (sum_attribute_decision_number / all_cases_number) * entropy(
                [x / sum_attribute_decision_number for x in attribute_decision_number])

        return information_value

    def decision_class_information(self):
        all_cases_number = len(self.__decision_table)
        attributes = [dict(Counter(x)) for x in zip(*self.__decision_table)]
        return entropy([x / all_cases_number for x in attributes[-1].values()])

    def gain(self, attribute_index: int):
        return self.decision_class_information() - self.information(attribute_index)

    def split_info(self, attribute_index: int):
        attributes = [dict(Counter(x)) for x in zip(*self.__decision_table)]
        all_cases_number = len(self.__decision_table)
        return entropy([x / all_cases_number for x in attributes[attribute_index].values()])

    def gain_ratio(self, attribute_index: int):
        return self.gain(attribute_index) / self.split_info(attribute_index)

    def chose_best_attribute(self):
        best_value = 0
        best_index = 0
        for i in range(len(self.__attributes)):
            gain_info = self.gain_ratio(i)
            if gain_info > best_value:
                best_index = i
                best_value = gain_info

        return best_index
