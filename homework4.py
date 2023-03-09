# 自行輸入 row , column , grid size,預設為3, 4, 2
row = int(input('input the row number\n>'))
column = int(input('input the column number\n>'))
size = int(input('input the grid size\n>'))
def sep():
    # 進行第一行分隔好之運算, 第一個'＋'自行輸出 '-'數量受到size影響 ' + '數量 = row + 1 因此以下回圈進行判定
    print ('+', sep = '', end = '')
    for x in range (row):
        for y in range (size):
            print ('-',sep = '', end = '')
        print ('+', sep = '', end = '')
    print()
def middle():
    for i in range (column):
        for j in range (size):
            print ('|', sep = '', end = '')
            for k  in range (row):
                for l in range(size):
                    print ('?', sep= ' ', end = '')
                print('|', sep = '', end = '')
            print()
        sep()
def hw4():
    sep()
    middle()
hw4()