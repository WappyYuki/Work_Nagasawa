#3の倍数、5の倍数を判断するプログラム

seisuu=input("整数を入力してください：")
seisuu=int(seisuu)

#3の倍数、5の倍数を判断

if seisuu%3==0:
  if seisuu%5==0:
    print(f"{seisuu}は3の倍数かつ5の倍数です。")
  else:
    print(f"{seisuu}は3の倍数です。")
elif seisuu%5==0:
  print(F"{seisuu}は5の倍数です。")
else:
  print("")
  
  