def sum_of_digits(num):
    num_str = str(num)
    total_sum = 0
    for i in num_str:
        total_sum += int(i)

    return total_sum

num = 544
print(sum_of_digits(num))