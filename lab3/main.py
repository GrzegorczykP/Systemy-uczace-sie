from decision_tree import DecisionTree


def main():
    dt = DecisionTree('gielda.txt')
    print(dt.chose_best_attribute())


if __name__ == '__main__':
    main()
