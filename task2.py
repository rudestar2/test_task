#!/usr/bin/env python
# -*- coding: utf-8 -*-


def change_check(bills_list):
    """
    Проверка возможности выдачи сдачи
    :param bills_list: <list> список с номиналом банкнот.
    :return: <True> or <False>
    """
    ticket = 25
    cashbox = 0
    for i in bills_list:
        if i == ticket:
            cashbox += i
        else:
            change = i - ticket
            if cashbox >= change:
                cashbox -= change
            else:
                print('NO')
                return False
    print('YES')
    return True

change_check([25, 25, 25, 25, 25, 100, 100])
