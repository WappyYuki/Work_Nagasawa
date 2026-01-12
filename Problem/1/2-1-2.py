#関数で計算してみよう！！

def mysum(num):
    bIsMinus=False
    if num<0:
        bIsMinus=True
        num=abs(num)

    t=0
    for i in range(num+1):
        t+=i

    if bIsMinus:
        t*=-1

    return t

#メインの処理
n=int(input("数字を入力してください:"))
print(str(mysum(n)))








