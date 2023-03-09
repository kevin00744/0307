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
    # row = int(input('input the row number\n>'))
    # column = int(input('input the column number\n>'))
    # size = int(input('input the grid size\n>'))
    sep(row , size)
    middle(row ,column ,size)
hw4()