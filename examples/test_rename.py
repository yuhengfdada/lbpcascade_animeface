import os

j = 1

try:
    os.rename('aa.jpg','aa.jpg')
    j += 1
except:
    print('skipped')