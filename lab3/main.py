from decision_tree import DecisionTree
from discretion import Discretion


def main():
    # a = Discretion('raw_data.txt',
    #            [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False])
    # a.calculate()
    # a.sava_to_file('data.txt')

    dt = DecisionTree('data.txt')
    print(dt)


if __name__ == '__main__':
    main()
