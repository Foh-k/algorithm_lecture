import random


# 0~100の値を持つ15要素配列を乱数で生成
def make_randlist(n=15):
    return list(random.randrange(100) for _ in range(n))


# 挿入する.実装方法の関係上後ろから降順か比較をしている
def insertion_sort(lst):
    for i in range(1, len(lst)):
        idx = i
        while(idx > 0 and lst[idx - 1] > lst[idx]):
            tmp = lst[idx - 1]
            lst[idx - 1] = lst[idx]
            lst[idx] = tmp
            idx -= 1


def main():
    lst = make_randlist()
    print("ソート前")
    print(lst)
    insertion_sort(lst)
    print("ソート後")
    print(lst)


if __name__ == "__main__":
    main()
