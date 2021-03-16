def read_data():
    with open('gieldaLiczby.txt') as file:
        return list(map(lambda x: x.split('.'), file))


def main():
    print(read_data())


if __name__ == '__main__':
    main()
