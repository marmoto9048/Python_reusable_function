import os
 
def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print "---  new folder...  ---"
		print "---  OK  ---"
 
	else:
		print "---  There is this folder!  ---"
		
file = "G:\\xxoo\\test"
mkdir(file)             #调用函数
