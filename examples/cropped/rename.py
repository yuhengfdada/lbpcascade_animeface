import os

j = 1
for i in range(1,47050):
    s1 = str(i).zfill(5)
    s2 = str(j).zfill(5)
    try:
        os.rename('{}.jpg'.format(s1),'{}.jpg'.format(s2))
        j += 1
    except:
        print('skipped')