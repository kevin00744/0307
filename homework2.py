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
hw2()