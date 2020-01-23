#!/usr/bin/python

import sys


# cache = {i: 0 for i in range(n + 1)}
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cash_moni=None):
    if cash_moni is None:
        cash_moni = {0: 1, 1: 1, 2: 2}
    if n not in cash_moni:
        cash_moni[n] = eating_cookies(n - 1, cash_moni) + eating_cookies(n - 2, cash_moni) + eating_cookies(n - 3, cash_moni)
    return cash_moni[n]
    # # Non cash_moni way #########################
    # if n == 0:
    #     return 1
    # elif n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # else:
    #     return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
