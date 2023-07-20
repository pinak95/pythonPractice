def max_range(n):
    if n == 1:
        return 1
    result = 0
    l, r = 1, int(n ** 0.5)
    for i in range(l, r + 1):
        if n % i == 0:
            result += 1
        else:
            break
    return result


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    print(max_range(n))
