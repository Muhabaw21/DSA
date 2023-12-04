def meeraArra(numbers):
    count =0
    found= False
    meeraStart = 0
    meeraEnd = 0

    for num in numbers:
        if num % 2 != 0:
            found = True
            break
    odd_flag =False
    for num in numbers:
        if num % 2 == 0 and not odd_flag:
            meeraStart += 1
        else:
            odd_flag = True
    for num in reversed(numbers):
        if num % 2 == 0:
            meeraEnd += 1
        else:
            break
    if meeraEnd == meeraStart and found:
        return True
    else:
        return False

