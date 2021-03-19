
b_w = []

def find_portfolio_options(sorted_quantization_list, static_tickers_len):
    n = len(sorted_quantization_list)
    l = print_All_K_Length(sorted_quantization_list, "", n, static_tickers_len)
    print(len(l))
# The main recursive method
# to print all possible
# strings of length k
def print_All_K_Length(sorted_quantization_list, prefix, n, k):
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
        if round(the_sum, 30) == 1:
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
        print_All_K_Length(sorted_quantization_list, newPrefix, n, k - 1)


def find_quantization_list(portfolio_quantization):
    sorted_quantization_list = [None] * (portfolio_quantization + 1)
    sorted_quantization_list[0] = 0.0
    i = 1
    while i <= portfolio_quantization:
        sorted_quantization_list[i] = ((i) / portfolio_quantization)
        i = i + 1
        return sorted_quantization_list

if __name__ == '__main__':  # You should keep this line for our auto-grading code.

    q = find_quantization_list(10)


    find_portfolio_options(q, 5)
