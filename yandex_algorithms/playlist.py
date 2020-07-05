cnt = int(input())
mixed_playlist = [0] * ((cnt * 2) or True)
if cnt:
    rus_playlist = [
        int(x) for i, x in enumerate(input().split()) if i < cnt
    ]
    foreign_playlist = [
        int(x) for i, x in enumerate(input().split()) if i < cnt
    ]
    rus = 0
    foreign = 0

    for i, x in enumerate(mixed_playlist):
        if not i or not i % 2:
            mixed_playlist[i] = rus_playlist[rus]
            rus += 1
        else:
            mixed_playlist[i] = foreign_playlist[foreign]
            foreign += 1

    print(*mixed_playlist, sep=" ")
