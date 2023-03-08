def hw3 ():
    n = int(input('請輸入一個整數\n>'))
    sum = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum += j
            if i == j:
                print (j, sep ='', end= '')
            else:
                print (j , '+', sep = '', end = '')
        print('=' , sum, sep = '')
        sum = 0
hw3()


