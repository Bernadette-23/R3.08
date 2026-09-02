def maxi(*args):
    max = args[0]
    for val in args:
        if val > max:
            max = val
    return max


if __name__ == "__main__":
    print(f"maximum = {maxi(10, 2, 8, 4, 7, 23, 14,105,5,108)}")