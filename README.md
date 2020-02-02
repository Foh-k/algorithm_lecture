# テスト範囲

1. 探索(2)
2. 文字列探索
3. ソート

## 探索
### ハッシュ法
ハッシュ法はデータの数によらず低数時間でデータのの挿入・削除・探索が行えるデータ構造.
キーの値をデータと関連付けることにより実現.そのような関連付ける方法を**ハッシュ関数**,
その関数により得られる値を**ハッシュ値**という.
しかしその関数により得られる値が別の入力に対して同じ出力が得られてしまうことがある.
これを**衝突**といい,衝突を回避する具体的な方法として次の二通りのアルゴリズムが存在.
1. チェイン法\
同じハッシュ値を持つものを連結リストとして繋ぐ,ハッシュ値を求めたあとには線形探索で値を見つける.
この方法の問題点はハッシュ値の重複が多くなると連結リストの線形探索がボトルネックとなり高速性が失われるということ.
最悪計算量はO(N),平均計算量はO(1 + N/B)これはB >> NならばO(1)だがN >> BのときO(N)になる.
ただしNはデータ数,Bはバケット数.\
[チェイン法の実装](https://github.com/Foh-k/algorithm_lecture/blob/master/chain.py)
2. オープンアドレス法\
衝突が起きた際に新たなハッシュ関数h_k(x)を利用して再度ハッシュ値を求める方法.
具体的には最初にh_1(x)を利用してハッシュ値を計算,もしそのバケットが既に利用されていた場合には
次のハッシュ関数h_2(x)を利用して新たなハッシュ関数を計算する.
この工程を空バケットが見つかるまで繰り返して行う.
問題点としてはバケットの数と同じ数のハッシュ関数を作ることが困難な点,及び格納するデータの数が多くなるに
つれてパフォーマンスが低下すること.\
[オープンアドレス法の実装](https://github.com/Foh-k/algorithm_lecture/blob/master/open_address.py)

## 文字列探索
探索対象の文字列(**テキスト**)から目的の文字列(**パターン**)を見つける.
具体的には次の3種類の方法が有名
1. 力任せ\
先頭から1文字づつ比較する線形探索的な手法.テキスト長をn,パターン長をmとすると最悪計算量はO(nm)
平均計算量はO(n)となる.なんだかんだ便利だからnがあんまり大きくないときはよく使われている.実装が楽だし.\
[力任せ法の実装](https://github.com/Foh-k/algorithm_lecture/blob/master/brute_force.py)
2. KMP法\
Knuth-Morris-Pratt法の略.全部人名だし正式名称は覚えなくていい.
直前の比較結果を利用してジャンプをすることで効率化を図る.
前処理としてテーブルを用意し,ずらす量を求めておく必要がある.
テーブルで与える情報としてはずらす量と次の開始地点.
ちょっとテーブル作成は面倒なので具体例を用いて解説してみる.
+ 例えばpattern = "tartar"の場合
    + 1文字目で失敗 → 1つずらしてパターンの0文字目から次の照合を開始する.(力任せ法と同じ)
    + 2文字目で失敗 → 失敗文字はtかもしれないので1文字ずらしてパターンの0文字目から照合開始.(この時点でも力任せ法と同じ動作)
    + 3文字目で失敗 → 前の2文字は"ta"であるとわかっているので位置文字ずらした場合は't'と'a'の比較になることは明白.したがって2文字ずらすことで効率的になる.また比較位置は0文字目から照合する.
    + 4文字目で失敗 → 3文字目の場合と同じように考えて3文字ずらすことができる
    + 5文字目で失敗 → 3,4文字目と同じように4文字ずらそうとすると,以前に一度出ている't'が無視されてしまう.すわなち現在わかっているテキスト中の文字列は"tart?"であるが,4文字ずらしてしまうと照合が'?'ぶぶんから始まり,'t'が一致する可能性があるのにスキップされてしまう.これを避けるためにはこの場合は不一致部分の3文字分ずらし,更に0文字目の't'が一致することは明らかなので1文字目から比較を開始する
    + 6文字目で失敗 → 5文字目で失敗した場合と同様に考えてずらす文字は3文字であり,最初の2文字"ta"は一致することは明らかなため2文字目から照合を行う.

以上のことをまとめると次のテーブルのようになる.

| 失敗位置(文字目) | ずらす量 | 次の開始位置(インデックス) |
|------------------|----------|--------------|
| 1                | 1        | 0            |
| 2                | 1        | 0            |
| 3                | 2        | 0            |
| 4                | 3        | 0            |
| 5                | 3        | 1            |
| 6                | 3        | 2            |

計算量は既にわかっている部分を再度比較することはない(ポインタた後戻りしない)ため最悪でもO(n)となる.
これは数字の上では力任せ法より高速であるが,力任せ法も平均計算量はO(n)であるため,前処理の必要性がある分
KMP法の方が低速になることもある.また実装が複雑なため実用性はあまり高くはない.\
[KMP法の実装](https://github.com/Foh-k/algorithm_lecture/blob/master/kmp.py)

3. BM法\
Boyer-Moore法の略,これも人名.新しいアルゴリズム見つけたら自分の名前つけてもいいのかな.つけてみたい.
KMP法の上位互換的な立ち位置.KMP法は先頭から比較を行ったがBM法は末尾から比較を行う.パターン文字列が全部違う文字だった場合パターン分(m文字)一気にすっとばせることからも末尾比較のが早くなるのはまぁなんとなくイメージしやすいかも.これもスキップする量の管理にテーブルを利用するが,その実装方法はKMP法とは全然違う.実装はしやすい.テーブルは比較した文字が何だったかに依存し,何文字ずらすかを決定する.
    1. 最初に256(1byte = char型のサイズ)分だけテーブルを確保
    2. テーブルをパターン文字列長mで初期化
    3. パターン文字列を先頭から**末尾-1**までイテレートし,その文字について値を**m - i - 1**で上書きする.-1をつけるのは配列のインデックスが0から始まるから.末尾を含まないのはポインタの逆戻りを避けるため.

一応具体例
パターン文字列が"abdebf"のとき
1. 256要素の配列skip[256]を用意
2. 0文字目から4文字目までのイテレート
3. 0文字目は'a'なのでskip[a]番目に6-1-0を代入
4. 1文字目から4文字目までも同様にやると次の通り

| 失敗文字 | ずらす量 |
|----------|----------|
| a        | 5        |
| b        | 1        |
| d        | 3        |
| e        | 2        |
| それ以外 | 6        |

[BM法の実装](https://github.com/Foh-k/algorithm_lecture/blob/master/bm.py)

## ソート
ソートには2種類ある.安定であるソートとそうでないソートである.
具体的には同じ要素の並び順が保持されるのが安定ソートであり,それを保証しないものが安定ソート以外のものである.
1. バブルソート\
最も単純なソートだが計算量はO(n^2)となってしまい低速.
要素数が少ないなら書きやすいし使うことはあるかもしれない.
アルゴリズムは次
    1. 末尾から順にスキャン
    2. もし大小の順序がa[k] > a[k+1]なら2要素をスワップ
    3. 配列の要素数を一つ減らして要素数が1になるまで1, 2を繰り返す
もちろん安定ソートである.

[バブルソートの実装](https://github.com/Foh-k/algorithm_lecture/blob/master/bubble_sort.py)

2. 選択ソート\
これも低速なソートアルゴリズム.書くのは多分一番簡単.頑張れば3行くらいでかけそう.
アルゴリズムは次
    1. 配列の中で最小要素を選ぶ
    2. 先頭に持ってくる
    3. 配列の要素を一つ減らし1つになるまで1,2を繰り返し.
もちろんこれも安定ソート

[選択ソートの実装](https://github.com/Foh-k/algorithm_lecture/blob/master/selection_sort.py)

3. 挿入ソート
これも低速ソート.先頭から順番に値を挿入していくようにソートを行う.
アルゴリズムは次の通り.
    1. 先頭1要素をソート済み配列として用意 
    2. 2要素目を挿入し,順序が満たされるまで隣接した要素同士を交換する.
    3. 2.をn要素目まで行う.
これも安定ソート

[挿入ソートの実装](https://github.com/Foh-k/algorithm_lecture/blob/master/insertion_sort.py)

4. シェルソート\
一言でいうと改良版挿入ソート.計算量は未解決問題の一つ.
アルゴリズムは次
    1. 適当なhを決める
    2. hごとに取り出した配列に対して挿入ソートを実行
    3. hを小さくして1になるまで繰り返し

このときのhの決め方に計算量は割と依存しているとわかっておりh = 3k + 1 (kは整数)の逆順に決めると解析的にO(n^1.25)程度, h = 2^k - 1 (kは整数)の逆順に決めるとO(n^1.5)程度の計算量で高速に実行ができるとわかっている.

5. コムソート\
6. クイックソート\
7. ヒープソート\
8. マージソート\