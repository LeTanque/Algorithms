#!/usr/bin/python
import argparse


def find_max_profit(prices):
    max_profit = 0
    current_min_price_so_far = 0
    current_max_sell = 0

    # This just adds prices together to create a big min price
    for i in range(0, len(prices)):
        current_min_price_so_far = current_min_price_so_far + prices[i]

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
    #     if prices[r] < prices[r + 1] and prices[r] < current_min_price_so_far:
    #         print('prices[r]: ', prices[r])
    #         current_min_price_so_far = prices[r]
    #         current_max_sell = 0
    #         for s in range(r + 1, len(prices)):
    #             print('every s in second loop: ', s)
    #             if prices[s] > current_min_price_so_far and prices[s] > current_max_sell:
    #                 current_max_sell = prices[s]
    #                 current_max_profit = current_max_sell - current_min_price_so_far
    #                 print('max_profit: ', max_profit)
    #                 if current_max_profit > max_profit:
    #                     max_profit = current_max_profit

    for r in range(0, len(prices)):
        print('all the r: ', r)



    print('current_min_price_so_far: $', current_min_price_so_far)
    print('current_max_sell: $', current_max_sell)
    print('max_profit >>>: ', f'${max_profit}')
    max_profit = current_max_sell - current_min_price_so_far
    print('max_profit after max - min >>>', f'${max_profit}')

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
