# This is a sample Python script.
from count_digit import countDigit
from find_max_in_list import findMaximum
from meera_array import meeraArra

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = countDigit(32121, 1)
    print("The count is:", result)  # Output: 2
    numbers = [5, 2, 9, 123, 7]
    maximum = findMaximum(numbers)
    print(maximum)
    meeraNum = [4, 8, 6, 3, 2, 9, 8, 11, 8, 13, 12, 12, 6, 24]
    meeraNumber = meeraArra(meeraNum)
    print("Meera:", meeraNumber)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
