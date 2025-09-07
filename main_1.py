# чтение файла с записанными ранее координатами
from time import sleep

i = 0
with open('gnss.txt', 'r') as f:
    nums = f.read().splitlines()
len_nums = len(nums)
while i < len_nums:
    num_csv = nums[i].split(',')
    time_now = num_csv[1]
    time_now = time_now[2:8]
    time_now_hh = time_now[:2]
    time_now_mm = time_now[2:4]
    time_now_ss = time_now[4:6]
    print(time_now, ' - ', time_now_hh, ':', time_now_mm, ':', time_now_ss)
    sleep(1)
    i += 1