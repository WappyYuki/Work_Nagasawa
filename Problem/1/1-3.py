#偶数か奇数を判断するプログラム

#数値の入力
seisuu=input("整数を入力してください。：")
seisuu=int(seisuu)

#偶数か奇数か判断

if seisuu%2==0:
  print(f"{seisuu}は偶数です。")
else:
  print(f"{seisuu}は奇数です。")