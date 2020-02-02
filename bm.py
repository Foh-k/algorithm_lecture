import random
import string
import sys
# BM法の実装.標準入力から探索したい文字列を入力してあるかを判定.


# 100文字分
def make_random_string(n=100):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))


# テーブルの作成.KMP法の1億倍簡単. -1を忘れないように！！
def make_table(pat):
    table = list(len(pat) for _ in range(100))
    for i in range(len(pat) - 1):
        table[ord(pat[i])] = len(pat) - i - 1
    return table


# 探索部.テーブルの+1を忘れないように
def bm_search(s, pat):
    table = make_table(pat)
    print(table)
    i, j = len(pat) - 1, len(pat) - 1
    while i < len(s):
        while j > 0:
            if s[i] == pat[j]:
                i -= 1
                j -= 1
                continue
            else:
                i += table[ord(s[i])]
                j = len(pat) - 1
                break
        if j == 0:
            return i - j

    return -1


def main():
    s = make_random_string()
    print(s)
    pat = input()
    loc = bm_search(s, pat)
    if loc >= 0:
        print(loc)
    else:
        print(":(")


if __name__ == "__main__":
    main()
