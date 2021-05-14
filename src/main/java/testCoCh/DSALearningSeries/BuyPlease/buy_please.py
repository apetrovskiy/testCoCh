def buy_please(a: int, b: int, x: int, y: int) -> int:
    return a*x+b*y


if __name__ == '__main__':
    input = input().split(" ")
    a, b, x, y = map(int, input)
    print(buy_please(int(input[0]), int(
        input[1]), int(input[2]), int(input[3])))
