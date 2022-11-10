def sum_odd_position(list_num):
    list_len = len(list_num)
    sum = 0
    for i in range(1, list_len, 2):
        sum+=int(list_num[i])
    return sum