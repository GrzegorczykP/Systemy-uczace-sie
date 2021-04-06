class Node:
    def __init__(self):
        self.children = []
        self.decision_class = None
        self.test = None
        self.input_value = None

    def __str__(self):
        if self.decision_class is not None:
            return f'{self.input_value} -> Klasa decyzyjna "{self.decision_class}"\n'
        else:
            text = ''
            if self.input_value is None:
                text += f'KORZEŃ -> Węzeł (a{self.test})\n'
            else:
                text += f'{self.input_value} -> Węzeł (a{self.test})\n'

            for child in self.children:
                t = str(child)
                text += '\n'.join(map(lambda x: '\t' + x, t.strip().split('\n'))) + '\n'

            return text
