import random
# このチェイン法は結構適当なので値の重複処理をしてないことに注意
# つまり2回同じ値が入力されても2つ分テーブルに格納される

# mod10でハッシュを計算するためテーブルのサイズは10個
hash_table = [[]]
for i in range(9):
    hash_table.append([])


def hash(n):
    # ハッシュ関数には(n mod 10)を利用
    return n % 10


# 初期化処理
def store():
    lst = []
    for i in range(30):
        # リストの中身は乱数で適当に生成
        lst.append(random.randrange(1000))
    # ランダム生成したlstの中身をテーブルに格納
    for e in lst:
        hash_table[hash(e)].append(e)


# 格納状態の表示
def print_table():
    print("現在のテーブルの状態")
    for e in hash_table:
        print(e)


# 値の削除
def remove(target):
    hash_table[hash(target)].remove(target)


# 値の追加
def add(target):
    hash_table[hash(target)].append(target)


# 値の検索及び削除
def search(target):
    index = hash(target)
    if target in hash_table[index]:
        hash_table[index].remove(target)
        return True
    else:
        return False


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
