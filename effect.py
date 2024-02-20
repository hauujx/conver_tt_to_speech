import sys
import time
from alive_progress import alive_bar


"""def printProgressBar(value,max,label):
    n_bar = 40 #size of progress bar
    #max = 100
    j= value/max
    sys.stdout.write('\r')
    bar = '█' * int(n_bar * j)
    bar = bar + '-' * int(n_bar * (1-j))
    sysbmol ='/ \ |'
    sys.stdout.write(f"{label.ljust(10)} | [{bar:{n_bar}s}] {int(100 * j)}%  "+'\\')
    sys.stdout.flush()"""



with alive_bar(100) as bar :
    print('\x1b[6;30;42m' + 'Loadding : '+'\x1b[0m')
    for i in range(0,100):
        bar()
        time.sleep(0.04)

