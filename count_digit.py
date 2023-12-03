def countDigit(number, digit):
    count = 0
    if number <= 0:
        return 0
    while number > 0:
        module = number % 10
        if module == digit:
            count += 1
        number //= 10
    return count
