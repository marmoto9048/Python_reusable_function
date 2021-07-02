def read_file(file_path):
    f = open(file_path)
    line = f.readline()
    sentence_lst = []
    while line:
        try:
            # print(line)
            sentence_lst.append(line)
            # print('可读取')
        except:
            print('无法读取')
            pass
        line = f.readline()
    f.close()
    return sentence_lst
def save(file,data):
    filename = open(file,'a+')
    for value in data:
        filename.write(str(value)+'\n')
    filename.close()
    print('saved in ',file)

   
def n_line():
    f.writelines(lists) #1 是不换行的写入，可用以下方法在写入时换行。
    for line in lists:      #2  换行
        f.write(line+'\n')
