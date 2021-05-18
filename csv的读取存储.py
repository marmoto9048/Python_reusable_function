#节选自 处理符号.py
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

   
  
  
if __name__ == "__main__":
    file_path='10w-gpt2-to-clean.csv'
    output_file_path='out_put_corpus_for_t5.csv'
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
    # print('out_list', out_list)
    #将清理好的句子存进csv
    origin_sentence = [x[1] for x in sentence]   #将origin句子单独提取出来到list中
    out_list2 = list(zip(origin_sentence, out_list))
    # print('out_list2',out_list2)  #最终要被输出的句子   ：   原始的aclarc句子和gpt2润色后的句子
    save_to_csv(output_file_path,out_list2)
    print('完成！！！')
