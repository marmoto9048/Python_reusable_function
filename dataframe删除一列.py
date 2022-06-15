>>>df = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])

>>>df

   A   B   C   D

0  0   1   2   3

1  4   5   6   7

2  8   9  10  11

#Drop columns,两种方法等价

>>>df.drop(['B', 'C'], axis=1)

   A   D

0  0   3

1  4   7

2  8  11

>>>df.drop(columns=['B', 'C'])

   A   D

0  0   3

1  4   7

2  8  11

# 第一种方法下删除column一定要指定axis=1,否则会报错
>>> df.drop(['B', 'C'])

ValueError: labels ['B' 'C'] not contained in axis

#Drop rows
>>>df.drop([0, 1])

   A  B   C   D

2  8  9  10  11

>>> df.drop(index=[0, 1])

   A  B   C   D
   
2  8  9  10  11
