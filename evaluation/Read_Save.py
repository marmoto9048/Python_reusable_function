def read_file(read_file_path):
    f = open(read_file_path)
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

def save(output_file,data):
    filename = open(output_file,'a+')
    for value in data:
        filename.write(str(value)+'\n')
    filename.close()
    print('saved in ',output_file)

