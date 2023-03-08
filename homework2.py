def hw2 ():
  n = int(input('輸入大小：\n>'))
  # n = 5
  s = n * 2 + 1 
  for i in range (s):
    for j in range(s):
      if i==j or i+j+1 == s:
        print('x', end = '')
      else:
        print(' ', end = '')
    print('\n')

hw2()