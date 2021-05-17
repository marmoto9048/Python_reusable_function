from transformers import AutoTokenizer, AutoModelWithLMHead

import torch
def use_model_data_argument(input_query):
    if torch.cuda.is_available():
        device = torch.device("cuda")
    else :
        device = "cpu"

    tokenizer = AutoTokenizer.from_pretrained("salesken/paraphrase_generation")
    model = AutoModelWithLMHead.from_pretrained("salesken/paraphrase_generation").to(device)

    # for i in range(len(input_query)):
    query= input_query + " ~~ "

    input_ids = tokenizer.encode(query.lower(), return_tensors='pt').to(device)
    sample_outputs = model.generate(input_ids,
                                    do_sample=True,
                                    num_beams=1,
                                    max_length=128,
                                    temperature=0.9,
                                    top_p= 0.99,
                                    top_k = 3,
                                    num_return_sequences=40)
    paraphrases = []#Paraphrase-any-question-with-T5-Text-To-Text-Transfer-Transformer--master/checkpointepoch=0.ckpt
    # print('sample_outputs',sample_outputs)  #sample_outputs:40 lines
    # r=sample_outputs[1]
    r = tokenizer.decode(sample_outputs[1], skip_special_tokens=True).split('||')[0]
    r = r.split(' ~~ ')[1]
    # print('r-after',r)
    return r
# print('sample_outputs[1]',sample_outputs[1])
# for i in range(len(sample_outputs)):
#     print('r-before', i)
#     r = tokenizer.decode(sample_outputs[i], skip_special_tokens=True).split('||')[0]
#     r = r.split(' ~~ ')[1]
#     # print('r',r)
#     if r not in paraphrases:
#         paraphrases.append(r)
# print('len',len(paraphrases),'len(sample_outputs)',len(sample_outputs))
# for i in range(len(paraphrases)):
#     print(i,paraphrases[i-1])
# print(paraphrases)
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

if __name__=='__main__':
    input_file_path = "test-100.txt"
    output_file_path= "2.txt"
    # input_query=["every moment is a fresh beginning","one moment is a fresh beginning","tomorror morning is a fresh beginning"]
    output_list=[]

    input_query=read_file(input_file_path) #1 读取文件
    print('input_query',input_query)
    for i in range(len(input_query)):
        output_list.append(use_model_data_argument(input_query[i]))  # 2 使用model转换1中的文件list
        if i%5==0:
            print('正在处理第：',i)
    save(output_file_path, output_list)
    print('output_list',len(output_list))
    print('完成！')


