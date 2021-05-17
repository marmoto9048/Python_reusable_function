def read_file(file_path):
    f = open(file_path)
    line = f.readline()
    sentence_lst = []
    while line:
        try:
            print(line)
            sentence_lst.append(line)
            print('可读取')
        except:
            print('无法读取')
            pass
        line = f.readline()
    f.close()
    return sentence_lst
