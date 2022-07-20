#!/usr/bin/env python
# coding: utf-8
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import nltk
import pandas as pd

modelPath = 'pytorchOutput'
model = GPT2LMHeadModel.from_pretrained(modelPath)
model.eval()
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")

def generateSentence(sentence):
    generated = tokenizer.encode(sentence)
    context = torch.tensor([generated])
    past = None

    for i in range(25):
        print(i)
        output, past = model(context, past=past)
        token = torch.argmax(output[..., -1, :])

        generated += [token.tolist()]
        context = token.unsqueeze(0)
        sequence = tokenizer.decode(generated)
        print(sequence)
        
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


if __name__ == '__main__':
    input_file_path = "data/trainset.txt"  
    output_file_path= "data/remake3.csv"
    # input_query=["every moment is a fresh beginning","one moment is a fresh beginning","tomorror morning is a fresh beginning"]
    output_list=[]
    #
    input_query=read_file(input_file_path) #1 读取文件
    print('input_query',len(input_query))
    for i in range(len(input_query)):
        out_sentence=generateSentence(input_query[i])
        output_list.append(out_sentence)  # 2 使用model转换1中的文件list
        if (i+1)%50==0:
            print('正在处理第：',i - 49,'~', i + 1)
            print('input_query[]', i - 49, i + 1, input_query[i - 49:i + 1])
            print('output_list[]', i - 49, i + 1, output_list[i - 49:i + 1])
    z = list(zip(input_query, output_list))
    # print('z',z)
    test = pd.DataFrame(data=z)
    test.to_csv(output_file_path, encoding='utf-8',mode='a', header=False)

    print('output_list',len(output_list))
    print('完成！')



