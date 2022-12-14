import sys

num = int(input())

max_num = -sys.maxsize
total_sum = 0

for i in range(1, num + 1):
    current_num = int(input())

    total_sum = total_sum + current_num

    if current_num > max_num:
        max_num = current_num

other_nums_sum = total_sum - max_num

if other_nums_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    diff = abs(other_nums_sum - max_num)
    print('No')
    print(f'Diff = {diff}')