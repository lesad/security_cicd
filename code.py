import random

def main():
    # craete a list of 10 random numbers
    list1 = [random.randint(0, 100) for i in range(10)]

    # do some erronous things
    x = list1[300]

    with open("test.txt", "r") as f:
        f.write("Hello World")

if __name__ == "__main__":
    pass
