os.path.join()函数用于路径拼接文件路径。
os.path.join()函数中可以传入多个路径：

会从第一个以”/”开头的参数开始拼接，之前的参数全部丢弃。

以上一种情况为先。在上一种情况确保情况下，若出现”./”开头的参数，会从”./”开头的参数的上一个参数开始拼接。

import os

print("1:",os.path.join('aaaa','/bbbb','ccccc.txt'))

print("2:",os.path.join('/aaaa','/bbbb','/ccccc.txt'))

print("3:",os.path.join('aaaa','./bbb','ccccc.txt'))


输出为

1: /bbbb\ccccc.txt
2: /ccccc.txt
3: aaaa\./bbb\ccccc.txt
 
