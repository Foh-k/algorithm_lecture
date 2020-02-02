import random
import numpy


# 0~100の値を持つ15要素配列を乱数で生成
def make_randlist(n=15):
    return list(random.randrange(100) for _ in range(n))


# 計算量はO(n^2)になる.遅い！
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(len(lst) - i):
            if lst[min_idx] > lst[i + j]:
                min_idx = i + j
        tmp = lst[i]
        lst[i] = lst[min_idx]
        lst[min_idx] = tmp


def main():
    lst = make_randlist()
    print("ソート前")
    print(lst)
    selection_sort(lst)
    print("ソート後")
    print(lst)


if __name__ == "__main__":
    main()
