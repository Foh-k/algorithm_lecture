import random


# mod10でハッシュを計算するためテーブルのサイズは10個
# また値は-1で初期化して値が-1ならば未使用とする
hash_table = []
for i in range(10):
    hash_table.append(-1)


# ハッシュ関数はk回目のものが(n + k mod 10)
def hash(x, k=0):
    return (x + k) % 10


# 格納状態の表示
def print_table():
    print("現在のテーブルの状態")
    for e in hash_table:
        print(e)


def store():
    lst = []
    for i in range(10):
        # リストの中身は乱数で適当に生成
        lst.append(random.randrange(10000))
    # ランダム生成したlstの中身をテーブルに格納
    for e in lst:
        k = 0
        while hash_table[hash(e, k)] != -1:
            k += 1
        hash_table[hash(e, k)] = e


# 面倒だから書いてないけどちゃんと存在しなかった場合のエラー処理はいる
def remove(target):
    k = 0
    while hash_table[hash(target, k)] != target:
        k += 1
    hash_table[hash(target, k)] = -1


def add(target):
    k = 0
    while hash_table[hash(target, k)] != -1:
        k += 1
    hash_table[hash(target, k)] = target


def search(target):
    k = 0
    while hash_table[hash(target, k)] != target:
        if k >= 10:
            return False
        k += 1
    hash_table[hash(target, k)] = -1
    return True


def main():
    store()
    print_table()
    print("削除する値の入力")
    rm = int(input())
    remove(rm)
    print_table()
    print("追加する値の入力")
    insert = int(input())
    add(insert)
    print_table()
    print("検索する値の入力")
    num = int(input())
    if(search(num)):
        print("Exist!!")
    else:
        print(":(")


if __name__ == "__main__":
    main()
