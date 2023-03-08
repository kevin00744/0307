row = int(input('input the row number\n>'))
column = int(input('input the column number\n>'))
size = int(input('input the grid size\n>'))
def sep():
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