def hw3 ():
    #n可以自行輸入（預設值為10) 相加 = sum
    # n = int(input('請輸入一個整數\n>'))
    n = 10
    sum = 0
    # 使用兩個回圈來進行判定因為需要從1開始到n 外層i為層數 分別是1, 1+2 內層j為相加之狀況,
    # j回圈判定：遇到i = j 進行輸出數字,當今天重新進行loop,發現i != j 則輸出 '+' sum每一次都進行運算,2; j回圈完成後 將 '=' sum 輸出 並將sum 設為 0 重心運算
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


