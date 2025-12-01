# 合計を格納する変数を初期化
total = 0

# 入力する数値の個数を指定
n = int(input("合計したい数値の個数を入力してください: "))

# for文で指定した回数だけ入力を受け取り、合計する
for i in range(n):
    num = int(input(f"{i+1}番目の数値を入力してください: "))
    total += num

# 結果を表示
print(f"{n}個の数値の合計は {total} です。")
