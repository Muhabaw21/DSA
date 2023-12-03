# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def findMaximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num>maximum:
            maximum=num
    return  maximum


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [5, 2, 9, 123, 7]
    maximum = findMaximum(numbers)
    print(maximum)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
