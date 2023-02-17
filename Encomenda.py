import itertools


def look_and_say(n):
    seq = "1"
    for i in range(n):
        seq = "".join(str(len(list(group))) + str(key) for key, group in itertools.groupby(seq))
        print(seq)
        print(i)
    return seq

print(look_and_say(10))
