#関数に変更

def mymoney(mon):
    i=1
    total=0
    while True:
       total+=i
       if total>=mon:
           break
       i+=1
    return i

#メイン情報
n=int(input("金額を入力してください："))
print(str(mymoney(n)))




        

