#貯金額N円を確認するのは何日目？

N=input("金額を入力してください：")
N=int(N)

#計算
i=1 #日数
total =0 #合計金額

while True:
    print(total)
    total+=i
    if total>=N:
        break
    i += 1
print(str(i))