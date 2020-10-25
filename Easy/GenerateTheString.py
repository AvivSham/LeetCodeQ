def generate_the_string(n: int) -> str:
    return 'a' * n if n % 2 == 1 else 'a' * (n - 1) + 'b'


if __name__ == '__main__':
    print(generate_the_string(5))
