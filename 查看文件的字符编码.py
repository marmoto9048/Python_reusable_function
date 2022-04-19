import chardet

f = open(data_path,'rb')
data = f.read()

print(chardet.detect(data))


>>> print(chardet.detect(data))
{'encoding': 'SHIFT_JIS', 'confidence': 0.99, 'language': 'Japanese'}
