def read_data():
    with open('agaricus-lepiota.data') as file:
        file_data = list(map(lambda line: line.strip().split(','), file))

    full_data = list(filter(lambda x: '?' not in x, file_data))
    part_data = list(filter(lambda x: '?' in x, file_data))

    return full_data, part_data


def calc_dist(t1, t2):
    dist = 0
    for i in range(len(t1)):
        if t1[i] != '?' and t2[i] != '?':
            dist += abs(ord(t1[i]) - ord(t2[i]))
    return dist


def main():
    full_data, part_data = read_data()

    filled = []
    for to_fill in part_data:
        best_full = []
        best_dist = calc_dist(to_fill, full_data[0])
        for full in full_data:
            dist = calc_dist(to_fill, full)
            if dist < best_dist:
                best_full = full
                best_dist = dist
        i = to_fill.index('?')
        temp = to_fill
        temp[i] = best_full[i]
        filled.append(temp)

    with open('zad1.out', 'w') as file:
        for data in full_data:
            file.write(','.join(data) + '\n')
        for data in filled:
            file.write(','.join(data) + '\n')


if __name__ == '__main__':
    main()
