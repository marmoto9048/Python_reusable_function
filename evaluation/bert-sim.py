#
from sentence_transformers import SentenceTransformer
from Read_Save import read_file

model = SentenceTransformer('paraphrase-distilroberta-base-v1')
sentences = ['This framework generates embeddings for each input sentence',
    'Sentences are passed as a list of string.',
    'The quick brown fox jumps over the lazy dog.']
sentence_embeddings = model.encode(sentences)
for sentence, embedding in zip(sentences, sentence_embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print("")
if __name__=='__main__':
    read_file_path = '1_NLU/test-100-output0-NLU.txt'
    target = '1_NLU/test-100.txt'
    out_file_path = '1_NLU/bert-out.txt'
    # input_query=["every moment is a fresh beginning","one moment is a fresh beginning","tomorror morning is a fresh beginning"]
    output_list=[]

    input_query=read_file(read_file_path) #1 读取文件
    print('input_query',input_query)
    for i in range(len(input_query)):
        output_list.append(use_model_data_argument(input_query[i]))  # 2 使用model转换1中的文件list
        if i%5==0:
            print('正在处理第：',i)
    save(out_file_path, output_list)
    print('output_list',len(output_list))
    print('完成！')

