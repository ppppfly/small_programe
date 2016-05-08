# coding=utf-8

import sys


def count_for_year(initial_amount, monthly, year_rate):
    monthly_rate = year_rate / 12
    count = 0
    while count < 12:
        count += 1
        initial_amount += monthly
        initial_amount *= 1 + monthly_rate
    return initial_amount

if __name__ == '__main__':

    args = sys.argv

    final_return = int(args[1])
    interest_rate = float(args[2])
    init_amount = int(args[3])
    monthly_input = int(args[4]) if len(args) > 4 else 0

    print '如果您一开始投入：', init_amount
    print '并且每个月坚持存入：', monthly_input
    print '找到一个年化利率为：', interest_rate * 100, '%的投资渠道'
    print '那么，收获您的第一个', final_return, '将在：'

    years = 0
    amount = init_amount

    while amount < final_return:
        years += 1
        amount += count_for_year(amount, monthly_input, interest_rate)
        print '第', years, '年的收益是：', amount

    total_input = init_amount + years * 12 * monthly_input
    print '如果你投入', init_amount, '，年收益率是', interest_rate, '，最终将获得', final_return, '的年月是', years, '年，此时的收益是：', amount
    print '总共投入', total_input, '总利息：', amount - total_input
    # 输入：python return_rate.py 1000000 0.1 10000 1000
