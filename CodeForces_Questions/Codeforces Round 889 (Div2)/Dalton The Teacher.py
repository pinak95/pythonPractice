def min_moves(n, perm):
    unhappy_students = sum(1 for i in range(n) if perm[i] == i + 1)
    return (unhappy_students // 2) + 1 if unhappy_students % 2 else unhappy_students // 2


t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    perm = list(map(int, input().split()))

    print(min_moves(n, perm))
