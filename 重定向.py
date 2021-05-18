if __name__ == '__main__':
    results_file='ppl/ppl-report/'
    filename='ppl-file2.txt'
    filename_path=os.path.join(results_file,filename)
    print('filename_path',filename_path)
    sys.stdout = open(filename_path, "w")  #将命令行输出重定向到日志文件中
