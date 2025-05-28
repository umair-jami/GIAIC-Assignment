def fibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
        return memo[num]

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(fibonacci(55))