import os


def read_data():
    with open('abalone.data') as file:
        return list(map(lambda line: line.strip().split(','), file))


def discretization_p(data: list):
    path = './zad2.out/przedzial/'
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass
    for i in range(1, 8):
        try:
            os.mkdir(path + str(i + 1))
        except FileExistsError:
            # directory already exists
            pass
        for j in range(10):
            with open(path + str(i + 1) + f'/[{j}, {j + 1}).txt', 'w') as file:
                filtered = list(filter(lambda x: j / 10 <= float(x[i]) < (j + 1) / 10, data))
                for x in filtered:
                    file.write(','.join(x) + '\n')


def discretization_cz(data: list):
    path = './zad2.out/czestosc/'
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass

    step = len(data) // 10
    for i in range(1, 8):
        try:
            os.mkdir(path + str(i + 1))
        except FileExistsError:
            # directory already exists
            pass
        sor = sorted(data, key=lambda x: x[i])
        slited = list_split(sor, 10)
        for j in range(10):
            with open(path + str(i + 1) + f'/{j}.txt', 'w') as file:
                for x in slited[j]:
                    file.write(','.join(x) + '\n')


def list_split(a, n):
    k, m = divmod(len(a), n)
    return list(a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def main():
    data = read_data()

    discretization_p(data)
    discretization_cz(data)


if __name__ == '__main__':
    main()
