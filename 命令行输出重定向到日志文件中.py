def log_print(results_file,filename):
    filename_path=os.path.join(results_file,filename)
    if not os.path.exists(results_file):
        os.makedirs(results_file)
    if not os.path.exists(filename):
        os.system(r"touch {}".format(filename))  # 调用系统命令行来创建文件
    sys.stdout = open(filename_path, "w")  #将命令行输出重定向到日志文件中
    print('saving in ',filename_path)
    return filename_path
  
if __name__ == '__main__':
  results_file='ppl/ppl-report/'
  filename='ppl-file2.txt'
  log_print(results_file,filename)    #程序开始的时候，将logging写入文件中
