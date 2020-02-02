import string
import random

# KMP法の実装.標準入力から探索したい文字列を入力してあるかを判定.


# 100文字分
def make_random_string(n=100):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(n))


# ずらす文字と次の開始位置のペアの配列を返す
# 結構複雑でめんどい.こんなもの使う気がしないしテストには出てほしくない.
def make_kmp_table(pat):
    # 必ず位置文字目はひとつだけずらして0番目からの照合になる
    skip = [0]
    start = [-1]
    for i in range(len(pat) - 1):
        # 各操作で考えらえる最大部分文字列からスキップ量を計算する
        # 具体的には先頭からk長の部分文字列と末尾からk長の部分文字列の一致性の確認
        # 一致する最大の長さを省ける照合数としてスキップ量は"インデックス-省く照合数"
        maxlen = start[i] + 1
        while True:
            if maxlen == 0 or pat[:maxlen] == pat[i - maxlen + 1:i + 1]:
                skip.append(i - maxlen)
                start.append(maxlen)
                break
            else:
                maxlen -= 1
    start[0] += 1
    return skip, start


# kmp法を使って探索.注意点はskipの+1を忘れないこと.
# なんかバグあると思う.同じ文字の連続とかに弱い感じのちょっと特定ができてないので放置
# というかまじで実装重い.とてもつらい.テストに出るな！出るんじゃねぇ！
def kmp_search(s, pat):
    skip, start = make_kmp_table(pat)
    i, j = 0, 0
    while i < len(s):
        while j < len(pat):
            if s[i] == pat[j]:
                i += 1
                j += 1
                continue
            else:
                i += skip[j] + 1
                j = start[j]
                break
        if j == len(pat):
            return i - len(pat)

    return -1


def main():
    s = make_random_string()
    print(s)
    print("検索したい文字列の入力")
    pat = input()
    loc = kmp_search(s, pat)
    if loc > 0:
        print(loc + 1)
    else:
        print(":(")


if __name__ == "__main__":
    main()
