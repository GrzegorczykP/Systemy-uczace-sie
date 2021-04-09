def disc_fun(data, sections=10):
    min_data = min(data)
    max_data = max(data)
    interval = (max_data - min_data) / 10
    out = []

    for value in data:
        for section in range(sections):
            if value <= min_data + interval * (section + 1):
                if section != 1:
                    print()
                out.append(section)
                break
        else:
            print()

    return out


class Discretion:
    def __init__(self, file_name, list_of_flags: list):
        with open(file_name) as file:
            self.__raw_data = tuple(map(lambda x: tuple(x.strip().split(',')), file))

        self.__list_of_flags = list_of_flags
        self.__data = None

    def calculate(self):
        transposed = list(zip(*self.__raw_data))
        out = []
        for index, list_of_flag in enumerate(self.__list_of_flags):
            if list_of_flag:
                out.append(disc_fun(list(map(float, transposed[index]))))
            else:
                out.append(transposed[index])

        self.__data = tuple(zip(*out))

    def sava_to_file(self, file_name):
        with open(file_name, 'w') as file:
            for x in self.__data:
                file.write(','.join(map(str, x)) + '\n')
