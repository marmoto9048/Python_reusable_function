import csv
import nltk
import numpy as np
def read_csv_file(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    # print(rows)  # 输出所有数据
    data = np.array(rows)  # rows是数据类型是‘list',转化为数组类型好处理
    # print("type shape: ", type(data), data.shape)
    # print("data:---", data[1][2])
    return data
import pandas as pd
def save_to_csv(output_file_path,data): #输入list
    test = pd.DataFrame(data=data)
    test.to_csv(output_file_path, encoding='utf-8', mode='a', header=False)
    print('saved in ',output_file_path)


def clean_sentence(sequence):
    # print("原始字符串为 : " + test_str)# 输出原始字符串
    new_str = ""
    a = sequence.find('<\ST')  # 移除<\START>字符
    # print('有没有找到：',a)
    if a == -1:
        new_str2= sequence.replace('\n', '').replace('\r', '')
    else:
        for i in range(0, len(sequence)):
            if i < a:
                new_str = new_str + sequence[i]
                new_str2 = new_str.replace('\n', '').replace('\r', '')
    # print("字符串移除后为 : " + new_str)
    return new_str2
if __name__ == "__main__":
    file_path='10w-to-clean.csv'
    output_file_path='output_corpus.csv'
    sentence=read_csv_file(file_path)
    sequence=[]
    for i in range(len(sentence)):
        # print('i',sentence[i][2])
        sequence.append(sentence[i][2])  #将target句子单独提取出来到list中  Quora_Paraphrasing_train.csv  Quora_Paraphrasing_val.csv
    # print('sentence---',type(sequence))
    out_list=[]
    for j in range(len(sequence)):
        new_str=clean_sentence(str(sequence[j]))   #清理掉<start  符号
        # print('new_str',new_str)
        out_list.append(new_str)
    #将清理好的句子存进csv
    origin_sentence = [x[1] for x in sentence]   #将origin句子单独提取出来到list中
    out_list2 = list(zip(origin_sentence, out_list))
    # print('out_list2',out_list2)  #最终要被输出的句子   ：   原始的句子和修改后的句子
    save_to_csv(output_file_path,out_list2)
    print('完成！')

