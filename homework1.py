def hw1 ():
    # HW1. 1+2+3+...+n=sum
    #定義sum（因為1在回圈之外因此sum起始是1)
    sum = 1 
    #輸入變數ｎ進行運算
    n = int(input('請輸入一個整數\n >'))
    # 因為1前面不加入=因此跳脫for迴圈進行print
    print (1, end='')
    #進行for回圈
    for i in range(2,n+1):
        sum += i
        print (f'+{i}',sep = '', end = '')
    # print過程及答案
    print('=',sum, sep ='', end = '') 
hw1(1)