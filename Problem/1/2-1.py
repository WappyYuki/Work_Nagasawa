def mysum(num):
    num += 1
    return num

if __name__ == "__main__":
    n = int(input("数値を入力してください:"))
    print("入力:" + str(n))
    
    # bIsMinus = False
    # if n < 0:
    #     bIsMinus = True
    #     n = abs(n)
        
    # t = 0
    # for i in range(n+1):
    #     t+=i
    
    # if bIsMinus :
    #     t *= -1

    # print(t)

    x = mysum(10)
    print(x)

    if n == 2:
        print("ok")


# (1 + 10) * 10 / 2