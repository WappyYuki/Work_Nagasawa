#0~nまでの自然和を出力するプログラム
#n=input("数字を入力してください：")
#n=int(n)
#print("入力"+str(n))

#0~nまでを足す

#t=0
#for i in range(n+1):
    #t+=i
   # print(t)
#print(t)

#数値入力

s=input("数字を入力してください：")
s=int(s)
print("入力："+str(s))

t=0
if s<0:
    for i in range((s*-1)+1):
        t+=i
    print("-"+str(t))
else :
    for i in range(s+1):
        t+=i
    print(t)
    


 