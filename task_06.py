def max_num(*numbers):
    max_num = numbers[0]
    for a in numbers:
        if a >= max_num:
            max_num = a
    return max_num

print(max_num(1, 22, 3,2))
