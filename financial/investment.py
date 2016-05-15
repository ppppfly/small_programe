# coding=utf-8

import math
import sys


# 代表了一笔投资
class Investment(object):
    def __init__(self, invest_period, amount, year_rate, current_time):
        # 投资的周期，单位是月
        self._period = invest_period
        # 投资的金额，单位是RMB
        self._amount = amount
        # 投资的年化利率
        self._yearly_rate = year_rate
        # 投资的进入时间，本案例中，以0为起始标记
        self._time_start = current_time
        # 投资的现金流记录，下标0为初始投资的金额（负数）
        self._cash_flow = [-amount, ]

    def get_interest_return(self):
        return self._amount * self._yearly_rate / 12

    def get_current_period(self, current_time):
        return current_time - self._time_start

    # 获取本期的收益
    def get_return_now(self, current_time):
        # 获取当前周期
        current_period = self.get_current_period(current_time)

        # 如果过期了，就从投资包中删除
        if current_period > self._period:
            return 0

        # 获取利息
        pay = self.get_interest_return()

        # 如果是最后一期，返回利息和本金
        if current_period == self._period:
            self.cash_flow_recoding(pay + self._amount)
            return pay + self._amount

        self.cash_flow_recoding(pay)
        return pay

    def cash_flow_recoding(self, amount):
        self._cash_flow.append(amount)

    def get_cash_status(self):
        cash = 0
        for flow in self._cash_flow:
            cash += flow
        return cash

    def check_is_over(self, current_time):
        return self.get_current_period(current_time) >= self._period

    def check_invest_period(self, package, current_time):
        if self.check_is_over(current_time):
            package.remove(self)

    # 获取当前投资的剩余资产
    def get_rest_property(self):
        # 分析当前剩余周期
        rest_period = self._period + 1 - len(self._cash_flow)
        pay = self.get_interest_return()
        return (rest_period - 1) * pay + self._amount

    # 获取当前投资的本金
    def get_init_amount(self):
        return self._amount

    def __str__(self):
        return "%s, 周期：%d" % (str(self._cash_flow), self._period)

if __name__ == '__main__':
    args = sys.argv
    target_amount = int(args[1])
    rate = float(args[2])
    init_amount = int(args[3])
    monthly_amount = int(args[4])
    period = int(args[5])
    if len(args) > 6:
        debt = int(args[6])
        debt_rate = float(args[7])
        debt_period = int(args[8])

    # 实际的收益
    cash_amount = 0
    # 时间轴（单位：月）
    month_period = 1
    # 投资包：涵盖手上的所有投资
    # 开始投资：创建第一份投资
    investment_package = [Investment(period, init_amount, rate, month_period), ]

    # 每个月的现金收益
    monthly_return = 0
    # 当前投资包的总资产
    total_property = 0
    # 当前投资包的总本金，即利息的基数
    total_init_amount = 0
    # 目标是：总资产超过target_amount
    while True:
        # while month_period < 20:
        # 时间在推移，往前一个月
        month_period += 1
        # 每个月现金收入，归零
        monthly_return = 0
        # 当前总资产，归零
        total_property = 0
        # 当前总本金，归零
        total_init_amount = 0

        # 检查投资包
        for invest in investment_package:
            # 获取本月收益
            monthly_return += invest.get_return_now(month_period)

        for invest in investment_package:
            invest.check_invest_period(investment_package, month_period)

        cash_amount += monthly_return

        # 检查现金账户，将100块意以外的资金取出
        new_investment = monthly_amount
        if cash_amount > 100:
            cash_to_invest = math.floor(cash_amount / 100) * 100
            new_investment += cash_to_invest
            print '第%d月，资金[%d]满了100，追加投资：%d' % (month_period, cash_amount, cash_to_invest)
            cash_amount -= cash_to_invest

        # 将所有可用资金，重新投入
        investment_package.append(Investment(period, new_investment, rate, month_period))

        # 计算当前总资产
        for i in investment_package:
            total_property += i.get_rest_property()
            total_init_amount += i.get_init_amount()

        print '第%d月，当前总本金：%d，当前总资产：%d，现金收入为：%d, 再次投资：%d' % (month_period, total_init_amount, total_property, monthly_return, new_investment)
        print '-------------------------------------------------------'

        if total_init_amount > target_amount:
            break

    print '您初始投入：%d，年化利息是：%d%%，投资周期是%d个月，如果您每个月坚持追加投资：%d元，那么，达到您的预定资产：%d' % (init_amount, rate * 100, period,monthly_amount, target_amount)
    print '将历时%d月[%d年%d月]，月现金收入为：%d' % (month_period, month_period / 12, month_period % 12, monthly_return)
    print '总共投入本金：%d，当前总本金：%d，当前总资产：%d' % (month_period * monthly_amount, total_init_amount, total_property)
    print '-------------------------------------------------------'
