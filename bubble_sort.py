import random


# 0~100の値を持つ15要素配列を乱数で生成
def make_randlist(n=15):
    return list(random.randrange(100) for _ in range(n))


def bubble_sort(lst):
    n = 1
    for _ in range(len(lst)):
        for i in reversed(range(n, len(lst))):
            if lst[i - 1] > lst[i]:
                # スワップって標準ライブラリにないんだね.
                tmp = lst[i - 1]
                lst[i - 1] = lst[i]
                lst[i] = tmp


def main():
    lst = make_randlist()
    print("ソート前")
    print(lst)
    bubble_sort(lst)
    print("ソート後")
    print(lst)


if __name__ == "__main__":
    main()
