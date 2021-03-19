# None of these imports are strictly required, but use of at least some is strongly encouraged
# Other imports which don't require installation can be used without consulting with course staff.
# If you feel these aren't sufficient, and you need other modules which require installation,
# you're welcome to consult with the course staff.

import numpy as np
import pandas as pd
import pandas_datareader.data as web
from datetime import date
import itertools
import math
import yfinance
from typing import List

b_w = []
"""
sorting:
Time complexity = https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/
quick = https://www.geeksforgeeks.org/quick-sort/
mearge = https://www.geeksforgeeks.org/merge-sort/
Insertion Sort = https://www.geeksforgeeks.org/merge-sort/
Selection Sort = https://www.geeksforgeeks.org/selection-sort/

"""

# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()
def find_portfolio_options(sorted_quantization_list, static_tickers_len):
    n = len(sorted_quantization_list)
    to_print_All_the_K_Length(sorted_quantization_list, "", n, static_tickers_len)


def s_t_b(t, x, b):
    s_t_list = []
    s_t = 1
    s_t_list.append(s_t)
    for day in range(t):
        s_t *= np.dot(x[day], b[day])
        s_t_list.append(s_t)
    return s_t_list


def func2_s_t_b(t, x, b):
    s_t = 1
    for day in range(t):
        s_t *= np.dot(x[day], b)
    return s_t


# The main recursive method
# to print all possible
# strings of length k
def to_print_All_the_K_Length(sorted_quantization_list, prefix, n, k):
    # Base case: k is 0,
    # print prefix
    if (k == 0):
        the_sum = 0
        prefix = prefix[1:]
        list1 = prefix.split(" ")
        list2 = []
        for i in list1:
            the_sum += float(i)
            list2.append(float(i))
        if round(the_sum, 5) == 1:
            b_w.append(list2)
        return b_w

    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
        # Next character of input added
        newPrefix = str(prefix) + " " + str(sorted_quantization_list[i])

        # k is decreased, because
        # we have added a new character
        to_print_All_the_K_Length(sorted_quantization_list, newPrefix, n, k - 1)


def find_x(data):
    # need to add 1 in all places
    x = np.array(data.pct_change())
    x[:, :] += 1
    return x


class PortfolioBuilder:

    def get_daily_data(self, tickers_list: List[str],
                       start_date: date,
                       end_date: date = date.today()
                       ) -> pd.DataFrame:
        """
        get stock tickers adj_close price for specified dates.

        :param List[str] tickers_list: stock tickers names as a list of strings.
        :param date start_date: first date for query
        :param date end_date: optional, last date for query, if not used assumes today
        :return: daily adjusted close price data as a pandas DataFrame
        :rtype: pd.DataFrame

        example call: get_daily_data(['GOOG', 'INTC', 'MSFT', ''AAPL'], date(2018, 12, 31), date(2019, 12, 31))
        """

        try:
            data = web.DataReader(tickers_list, 'yahoo', start_date, end_date)
            data = data['Adj Close']
        except:  # cheak if the requset didn't work
            raise ValueError
        data1 = data.isnull()
        if data1.values.any():
            raise ValueError
        data_np = data1.to_numpy()
        if np.any(np.isnan(data_np)):
            raise ValueError

        self.tickers_list_len = len(tickers_list)
        self.data = data
        self.x = find_x(self.data)
        self.x = np.delete(self.x, 0, 0)
        self.duration_in_days = self.x.shape[0]
        return self.data

    def find_quantization_list(self, portfolio_quantization):
        sorted_quantization_list = [None] * (portfolio_quantization + 1)
        sorted_quantization_list[0] = 0.0
        i = 1
        while i <= portfolio_quantization:
            sorted_quantization_list[i] = ((i) / portfolio_quantization)
            i = i + 1
        return sorted_quantization_list

    def find_universal_portfolio(self, portfolio_quantization: int = 20) -> List[float]:
        """
        calculates the universal portfolio for the previously requested stocks

        :param int portfolio_quantization: size of discrete steps of between computed portfolios. each step has size 1/portfolio_quantization
        :return: returns a list of floats, representing the growth trading  per day
        """

        def find_nominator(t):
            the_vector = [0] * self.tickers_list_len
            for b_w_option in b_w:
                mult = np.multiply(b_w_option, func2_s_t_b(t, self.x, b_w_option))
                the_vector = np.add(the_vector, mult)
            return the_vector

        def find_denominator(t):
            the_sum = 0
            for b_w_option in b_w:
                the_sum += func2_s_t_b(t, self.x, b_w_option)
            return the_sum

        sorted_quantization_list = self.find_quantization_list(portfolio_quantization)
        find_portfolio_options(sorted_quantization_list, self.tickers_list_len)  # after this line we have b_w
        one_over_num_of_stocks = 1 / self.tickers_list_len
        days = self.duration_in_days
        the_b_t_line = [one_over_num_of_stocks] * self.tickers_list_len
        all_b_t = [the_b_t_line]
        for t in range(1, days):
            nominator = find_nominator(t)
            denominator = find_denominator(t)
            the_b_t_line = nominator / denominator
            all_b_t.append(the_b_t_line)
        wealth = s_t_b(len(all_b_t), self.x, all_b_t)
        return wealth


    def find_exponential_gradient_portfolio(self, learn_rate: float = 0.5) -> List[float]:

        def find_func3_nominator(b_t, b_t_j, learning_rate, x_t, x_t_j):
            return np.multiply(b_t_j, math.exp((learning_rate * x_t_j) / (np.dot(b_t, x_t))))

        def find_func3_denominator(b_t, learning_rate, x_t, ticker_len):
            sum = 0
            for k in range(ticker_len):
                b_t_k = b_t[k]  # get the fisrt row of b_t and the k-th element (because b_t is 2 dim)
                x_t_k = x_t[k]
                sum += np.multiply(b_t_k, math.exp((learning_rate * x_t_k) / (np.dot(b_t, x_t))))
            return sum

        def func3_find_b_t_plus_1_j(b_t_j, t, j, b_t, ticker_len, learning_rate, x_t):
            x_t_j = x_t[j]
            # print("x_t_j" , x_t_j)
            nominator = find_func3_nominator(b_t, b_t_j, learning_rate, x_t, x_t_j)
            denominator = find_func3_denominator(b_t, learning_rate, x_t, ticker_len)
            return nominator / denominator


        one_over_num_of_stocks = 1 / self.tickers_list_len
        b_t_j = one_over_num_of_stocks  # for the first iteration
        days = self.duration_in_days
        all_b_t_2D_list = []
        the_b_t_line = [b_t_j] * self.tickers_list_len
        all_b_t_2D_list.append(the_b_t_line)  # this is the
        for t in range(days):
            the_b_t_line = []
            for j in range(self.tickers_list_len):  # inserting b_t_j to the b_t line
                next_Avar = func3_find_b_t_plus_1_j(all_b_t_2D_list[t][j], t, j, all_b_t_2D_list[t], self.tickers_list_len, learn_rate, self.x[t])
                the_b_t_line.append(next_Avar)
            all_b_t_2D_list.append(the_b_t_line)  # this is the
        the_s_t_b = s_t_b(days, self.x, all_b_t_2D_list)
        return the_s_t_b

        """
        calculates the exponential gradient portfolio for the previously requested stocks

        :param float learn_rate: the learning rate of the algorithm, defaults to 0.5
        :return: returns a list of floats, representing the growth trading  per day
        """


if __name__ == '__main__':  # You should keep this line for our auto-grading code.

    """ def printt():
        sorted_quantization_list = [0.0, 1.0]
        for value in sorted_quantization_list:
            print(value)
            printt()

    printt()
    """
    s = date.fromisoformat('2020-01-01')
    e = date.fromisoformat('2020-01-06')
    x = PortfolioBuilder()
    x.get_daily_data(['GOOG', 'AAPL', 'MSFT', 'FB', 'AMZN'], date(2018, 1, 1), date(2020, 5, 14))
    x.get_daily_data(['GOOG', 'AAPL', 'MSFT'], date(2018, 1, 1), date(2018, 2, 1))
    x.find_universal_portfolio(10)

    #x.find_exponential_gradient_portfolio()

# None of these imports are strictly required, but use of at least some is strongly encouraged
# Other imports which don't require installation can be used without consulting with course staff.
# If you feel these aren't sufficient, and you need other modules which require installation,
# you're welcome to consult with the course staff.

