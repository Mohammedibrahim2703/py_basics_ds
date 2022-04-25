from datetime import datetime
start = datetime.now()
end = datetime.now()
# First function (Note the use of xrange since this is in Python 2)
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n + 1):
        final_sum += x

    return final_sum

def sum2(n):
    """
    Take an input of n and return the sum of the numbers from 0 to n
    """
    return (n*(n+1))/2

if __name__ == '__main__':
    print(sum1(10))
    print(sum2(100))
    print(start - end, sum1(100))