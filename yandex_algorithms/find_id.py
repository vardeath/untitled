cnt = int(input())
if cnt in range(2, 10 ** 6):
    all_ids = set([x for x in range(1, cnt + 1)])
    current_ids = set([
        int(x) for i, x in enumerate(input().split()) if i < cnt - 2
    ])
    all_ids -= current_ids
    answer = list(all_ids)
    answer.sort()

    print(*answer, sep=' ')
