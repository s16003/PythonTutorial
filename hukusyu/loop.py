data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for文を使って合計を求める
total = 0
for x in data:
    total += x

print(total)

# data の中から偶数だけ表示する
for y in data[1::2]:
    print(y)