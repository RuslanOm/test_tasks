def merge(ls1, ls2, res, comp):
    i = 0
    j = 0
    k = 0

    while i < len(ls1) and j < len(ls2):
        if comp(ls1[i], ls2[j]):
            res[k] = ls1[i]
            i += 1
        else:
            res[k] = ls2[j]
            j += 1
        k += 1

    while i < len(ls1):
        res[k] = ls1[i]
        i += 1
        k += 1

    while j < len(ls2):
        res[k] = ls2[j]
        j += 1
        k += 1

    return res


def merge_sort(ls, comp=lambda x, y: x <= y):
    if len(ls) > 1:
        ls1 = ls[:len(ls) // 2]
        ls2 = ls[len(ls) // 2:]

        merge_sort(ls1)
        merge_sort(ls2)
        merge(ls1, ls2, ls, comp)


if __name__ == "__main__":
    # some test code
    a = list(map(int, input().split()))
    merge_sort(a)
    print(*a)
