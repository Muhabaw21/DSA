def findMaximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum=num
    return  maximum