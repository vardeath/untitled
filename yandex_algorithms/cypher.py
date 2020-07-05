number = int(input())
max_num = 10000


def cypher(num):
    encode = str(num)[::-1]
    if num < 0:
        encode = '-' + encode[:-1]
    return int(encode)


if abs(number) < max_num:
    print(cypher(number))
