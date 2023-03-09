def next_fibonacii(previous1, previous2, max_depth):
    print(f"Current number: {previous1} {previous2}")
    return next_fibonacii(previous2, previous1 + previous2)

if __name__ == '__main__':
    print("Please, input max depth:")
    max_depth = input()
    next_fibonacii(1, 1, max_depth)  # 5, 8f