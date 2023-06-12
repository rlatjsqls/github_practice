def sum(a, b, *args):
    res = 0
    for i in [a, b, *args]:
        res += i
    return res
