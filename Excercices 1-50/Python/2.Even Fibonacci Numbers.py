""" 
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


#easy 
def fibonacci(limit):
    a, b = 1, 2
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum

def main():
    limit = 4000000
    result = fibonacci(limit)
    print(result)  # ANS: 4613732



#using memoization
def fibonacci(n):
    memo={}

    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

def main():
    limit = 4000000
    even_sum = 0

    for i in range(1, limit):
        fib = fibonacci(i)
        if fib > limit:
            break
        if fib % 2 == 0:
            even_sum += fib

    print(even_sum)  # ANS: 4613732

if __name__ == "__main__":
    main()


#slow af
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    limit = 4000000
    even_sum = 0

    for i in range(1, limit):
        fib = fibonacci(i)
        if fib > limit:
            break
        if fib % 2 == 0:
            even_sum += fib

    print(even_sum)  # ANS: 4613732

if __name__ == "__main__":
    main()

