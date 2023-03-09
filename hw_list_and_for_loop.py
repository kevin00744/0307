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
def hw2 ():
  #n可以自行輸入（預設值為5)
  # n = int(input('輸入大小：\n>'))
  n = 5
  # 規則為左右對成一輸入值決定有多少個且一一中心
  # 畫方格以及以xy第四象限方式,右斜以及中心會剛好是x=y 另外之左斜方式方面 剛好＝2n+1 因此已回圈判斷
  s = n * 2 + 1 
  # i回圈y（直行）j回圈x(橫列)
  for i in range (s):
    for j in range(s):
      if i==j or i+j+1 == s:
        print('x', end = '')
      else:
        print(' ', end = '')
    print('\n')
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
def sep(row, size):
    # 進行第一行分隔好之運算, 第一個'＋'自行輸出 '-'數量受到size影響 ' + '數量 = row + 1 因此以下回圈進行判定
    print ('+', sep = '', end = '')
    for x in range (row):
        for y in range (size):
            print ('-',sep = '', end = '')
        print ('+', sep = '', end = '')
    print()
def middle(row ,column, size):
    for i in range (column):
        for j in range (size):
            print ('|', sep = '', end = '')
            for k  in range (row):
                for l in range(size):
                    print ('?', sep= ' ', end = '')
                print('|', sep = '', end = '')
            print()
        sep(row , size)
def hw4(row = 3, column = 4 ,size = 2):
    # 自行輸入 row , column , grid size, 因題目要求 3, 4, 2 因此先註解輸入位置並且帶入3 4 2 
    row = int(input('input the row number\n>'))
    column = int(input('input the column number\n>'))
    size = int(input('input the grid size\n>'))
    sep(row , size)
    middle(row ,column ,size)







print ('Home work 1:1+2+3+…+n=sum')
hw1()
print ('\nHome work 2: Number of x in an arm.(preset = 5)')
hw2()
print ('\nHome work 3: Two loop for number count.(preset = 10)')
hw3()
print ('\nHome work 4 : Print the grid. ( preset = row number (3), column number (4), and grid size (2))')
hw4()