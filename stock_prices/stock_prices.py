#!/usr/bin/python
import argparse


def find_max_profit(prices):
    # # We start with the first possible trade
    max_profit = prices[1] - prices[0]
    # current_buy_lo = prices[0]   # Starts out first price 1050
    # current_sell_hi = 0
    # current_max_profit = 0
    len_arr = len(prices)

    # # This just adds prices together to create a big min price
    # for i in range(0, len(prices)):
    #     current_buy_lo = current_buy_lo + prices[i]

    # # This time travels, so it doesn't work. Can't buy
    # # future low and subtract from previous high
    # for r in range(0, len(prices) - 1):
    #     for s in range(1, len(prices) - 1):
    #         # print('r: & s: \n', r, '\n', s)
    #         spreads.append(prices[r] - prices[s])
    #         # if prices[r] - prices[s] > 0:

    # # Attempt 3. Doesn't pass [1050 270 1540 3800 2 100]
    # #  does pass [1050 270 1540 3800 2]
    # for r in range(0, len(prices) - 1):
    #     if prices[r] < prices[r + 1] and prices[r] < current_buy_lo:
    #         print('prices[r]: ', prices[r])
    #         current_buy_lo = prices[r]
    #         current_sell_hi = 0
    #         for s in range(r + 1, len(prices)):
    #             print('every s in second loop: ', s)
    #             if prices[s] > current_buy_lo and prices[s] > current_sell_hi:
    #                 current_sell_hi = prices[s]
    #                 current_max_profit = current_sell_hi - current_buy_lo
    #                 print('max_profit: ', max_profit)
    #                 if current_max_profit > max_profit:
    #                     max_profit = current_max_profit

    # # Passes the arbitrary test I assigned, but not the actual test.
    # # Need to take a fresh look at this problem.
    # # fails [10, 7, 5, 8, 11, 9] , 6 (returns 4)
    # for r in range(0, len_arr - 1):
    #     if prices[r] < current_buy_lo:
    #         current_buy_lo = prices[r]
    #         for s in range(r + 1, len_arr):
    #             # print("rs -------> \n", r, "\n", s)
    #             if prices[s] > current_buy_lo and prices[s] > current_sell_hi:
    #                 current_sell_hi = prices[s]
    #                 current_max_profit = current_sell_hi - current_buy_lo

    # # Need to effectively start the first loop ahead
    # # Then the second loop is getting bigger
    # # This is like doing what I was doing but in reverse
    # # Needs to be 1 otherwise prices[0] - prices[0] could happen
    for r in range(1, len_arr):  
        print("index -->", r)
        print('price r: ', prices[r])
        print('max_profit: ', max_profit)
        for s in range(0, r):
            print('price in inner loop: ', prices[s])
            # If the outer loop price minus inner loop is
            # greater than the biggest profit recorded,
            # Replace the biggest profit with the difference
            # between outer and inner loop
            if prices[r] - prices[s] > max_profit:
                max_profit = prices[r] - prices[s]

    
    return max_profit







if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
