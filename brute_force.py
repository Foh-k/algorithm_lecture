import random
import string
# 力任せ法の実装.標準入力から探索したい文字列を入力してあるかを判定.


# 100文字分
def make_random_string(n=100):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))


# 文字列が存在するときは開始インデックス,存在しなければ-1を返す
def brute_force_search(s, pat):
    iter = 0
    while iter < len(s) - len(pat):
        if(s[iter:iter + len(pat)] == pat):
            return iter
        else:
            iter += 1

    return -1


def main():
    s = make_random_string()
    print(s)
    print("検索したい文字列の入力")
    pat = input()
    loc = brute_force_search(s, pat)
    if loc > 0:
        print(loc + 1)
    else:
        print(":(")


if __name__ == "__main__":
    main()
