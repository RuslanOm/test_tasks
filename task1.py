def is_even_binary(value):
    return bool(value & 1)


def is_even(value):
    return int(str(value)[-1]) % 2 == 0


if __name__ == '__main__':
    value = int(input())
    print(is_even(value))
    print(is_even_binary(value))
