# coding: utf-8

import math

if __name__ == '__main__':
    start_val = 1.0
    target_val = 2.0
    years = 12
    rate = 0.05

    # (1 + rate) ^ years = 2
    new_rate = math.pow(target_val, 1.0/years) - start_val
    new_rate_percent = new_rate * 100
    print("人均GDP从%s万美元增长到%s万美元, %s年时间, 每年GDP需要增加%.4s%%" % (start_val, target_val, years, new_rate_percent))

    new_years = math.log(target_val, start_val + rate)
    print("人均GDP从%s万美元增长到%s万美元, 每年增长率为%.5s%%, 需要%.2s年" % (start_val, target_val, rate*100, new_years))
