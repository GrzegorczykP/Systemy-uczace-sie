import os


def read_data():
    with open('ecoli.data') as file:
        return list(map(lambda line: line.strip().split(), file))


def split(data: list):
    path = './zad4.out/'
    try:
        os.makedirs(path)
    except FileExistsError:
        # directory already exists
        pass

    sor = sorted(data, key=lambda x: x[1])
    slited = list_split(sor, 4)
    for i in range(4):
        with open(path + f'/{i+1}.txt', 'w') as file:
            for x in slited[i]:
                file.write('\t'.join(x) + '\n')


def list_split(a, n):
    k, m = divmod(len(a), n)
    return list(a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def main():
    data = read_data()
    split(data)


if __name__ == '__main__':
    main()