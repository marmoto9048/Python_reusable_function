import kenlm
import os
import statistics
import sys
import kenlm
# model = kenlm.Model('lm/test.arpa')
#https://github.com/kpu/kenlm/blob/0c4dd4e8a29a9bcaf22d971a83f4974f1a16d6d9/python/kenlm.pyx
def cal_ppl(input_text):
    perplexity_list=[]
    model_path='/media/marmoto9048/SSPH-UA/lab/evaluation/language-model/model/aclarc_model.bin'
    # model = kenlm.Model(model_path)
    # print(model.score('this is a sentence .', bos=True, eos=True))

    model = kenlm.Model(model_path)
    lines=open(input_text, 'r').readlines()
    # print('-----------lines：---',lines[3])
    for i in range(len(lines)):
        print('i',lines[i])
        score=model.perplexity(lines[i])
        print('perplexity::',score)
        perplexity_list.append(score)
    # print(model.score(input_text, bos = True, eos = True))
    print(input_text,'的ppl列表：',perplexity_list)
    ppl_average=statistics.mean(perplexity_list)
    print('平均值：', ppl_average)
    # filename_path=log_print()
    # sys.stdout = open(filename_path, "w")
    return ppl_average



def log_print():
    results_file='ppl/ppl-report/'
    filename='ppl-file.txt'
    filename_path=os.path.join(results_file,filename)
    if not os.path.exists(results_file):
        os.makedirs(results_file)
    if not os.path.exists(filename):
        os.system(r"touch {}".format(filename))  # 调用系统命令行来创建文件
    return filename_path


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
    results_file='ppl/ppl-report/'
    filename='ppl-file.txt'
    filename_path=os.path.join(results_file,filename)
    print('filename_path',filename_path)
    sys.stdout = open(filename_path, "w")

    file_path1 = "/media/marmoto9048/SSPH-UA/lab/evaluation/language-model/ppl/"
    file_path_list=get_file_path_list(file_path1)
    print('file_path_list',file_path_list)
    print('len(file_path_list)',len(file_path_list))
    # print('file_path_list[0]',file_path_list[0])

    # cal_ppl(file_path_list[0])


    output_list = []
    for i in range(len(file_path_list)):
        output_list.append(cal_ppl(file_path_list[i]))  # 2 使用model转换1中的文件list
        print('-------------------------','正在处理第：', file_path_list[i],'-------------------------')
    print('output_list', len(output_list))
    print('output_list',output_list)
    print('完成！')