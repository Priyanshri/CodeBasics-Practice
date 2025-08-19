def sum_all(*args):
    total = 0
    print("Arguments received:", args)
    for num in args:
        total += num
    return total

total = sum_all(1,2,3,4,5)

print(f"Sum of all numbers: {total}")


def company_info(**kwargs):
    # if 'ticker' in kwargs:
    #     print("Ticker: ", kwargs['ticker'])
    # if 'ceo' in kwargs:
    #     print("CEO: ", kwargs['ceo'])
    # if 'revenue' in kwargs:
    #     print("Revenue:", kwargs['revenue'])
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


company_info(ticker='AAPL', ceo="Tim Cook", revenue="200 billion")
    

# def find_square(n):
#     return n*n

x = lambda a: a*a

print("enter a number to find its square:")
n = int(input())
print(f"square of {n} is {x(n)}")
print(x(3))  # Output: 9

x = lambda a: a**a
print((x(3)))  # Output: 27

x = lambda a, b: a + b
print(x(3, 5))  # Output: 8