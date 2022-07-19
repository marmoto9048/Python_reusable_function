#coding=utf8
import kenlm
import os
import statistics
import sys
def cal_ppl(input_text):
    perplexity_list=[]
    model = kenlm.Model('model.bin')
    lines=open(input_text, 'r').readlines()
    # print('-----------lines：---',lines[3])
    for i in range(len(lines)):
        print('i',lines[i])
        print('perplexity::',model.score(lines[i]))
        perplexity_list.append(model.score(lines[i]))
    # print(model.score(input_text, bos = True, eos = True))
    print(input_text,'的ppl列表：',perplexity_list)
    ppl_average=statistics.mean(perplexity_list)
    print('平均值：', ppl_average)
    log_print(input_text)
    return
def log_print(input_text):
    results_file='ppl-results/'
    file_path=os.path.join(results_file,input_text,'sys-file.txt')
    if not os.path.exists(results_file):
        os.makedirs(results_file)
    if not os.path.exists(file_path):
        os.system(r"touch {}".format(file_path))  # 调用系统命令行来创建文件
    sys.stdout = open(file_path, "w")

def findAllFile(file_path):
    for root, ds, fs in os.walk(file_path):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def get_file_path_list(file_path1):
    file_path_list=[]
    for i in findAllFile(file_path1):
        file_path_list.append(i)
        # print(i)
    return file_path_list

if __name__ == '__main__':
    file_path1 = "model/ppl"
    file_path_list=get_file_path_list(file_path1)
    print('file_path_list',file_path_list)
