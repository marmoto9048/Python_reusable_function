import logging
import os
from sentence_transformers import SentenceTransformer
import numpy as np
import scipy
import re
import statistics
import sys

def retr_sents(query, corpus):
    distance_cos_all=[]
    with open(query, 'r', encoding='UTF-8') as query:
        sents = [i.lower() for i in query.readlines()]
        with open(corpus, 'rb') as cor:
            resource = cor.readlines()
            num = 0
            if method == 'retr_sentbert':
                for s in sents:
                    num += 1
                    print('For sentence ' + str(num),s)
                    print('For query ' + str(num), resource[sents.index(s)])
                    distance_cos = retr_sentbert(s, resource)
                    print('distance_cos',distance_cos)
                    distance_cos_all.append(distance_cos)
                    # with open('results/' + str(num) + '_retrieved_sentences_bert.txt', 'wb') as target:

            else:
                print('Please input the method correctly.')
    print('distance_cos_all',distance_cos_all)
    print('平均值：',statistics.mean(distance_cos_all))

def file_match(input):
    pattern = re.compile('\S*\..+')
    if re.match(pattern, input) == None:
        return False
    else:
        return True
def save_corpus_vec(corpus_vec):
    f = open(save_vector, "w")
    f.write(str(corpus_vec))
    f.close


def get_corpus_vec(query, resource, target):
    np.set_printoptions(threshold=np.inf)
    for i in range(len(resource)):
        resource[i] = str(resource[i], encoding='utf-8')
    model = SentenceTransformer('bert-base-nli-stsb-mean-tokens')
    corpus_vec = model.encode(resource)  # corpus_vec语料库总向量
    save_corpus_vec(corpus_vec)


def read_corpus_vec():
    with open(save_vector, 'r', encoding='UTF-8') as justed_vector:
        corpus_vec = justed_vector.readlines()
        # print('corpus_vec-----------', corpus_vec)
def retr_sentbert(query, resource):  #query是单个句子
    # get_corpus_vec(query, resource, target)
    # read_corpus_vec()
    np.set_printoptions(threshold=np.inf)
    for i in range(len(resource)):
        resource[i] = str(resource[i])#, encoding='utf-8'
    model = SentenceTransformer('bert-base-nli-stsb-mean-tokens')
    corpus_vec = model.encode(resource)  # corpus_vec语料库总向量
    save_corpus_vec(corpus_vec)
    query_vec = model.encode([query])  # query:被查询的句子
    distances_all = []
    for v in corpus_vec:
        # print('query:', query, '\n', 'resource[0]', resource[0])
        distances = scipy.spatial.distance.cdist(query_vec, [v], "cosine")[0]
#该函数用于计算两个输入集合的距离，通过metric参数指定计算距离的不同方式得到不同的距离度量值
        # print('cosine-distances', distances)
        distances_all.append(float(distances))
    # print('distances_all[0]',distances_all[0])
    return distances_all[0]
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    save_vector = 'save_corpus_vec.csv'
    method = 'retr_sentbert'

    query = '6-t5/test-100.txt'
    corpus = '6-t5/test-100-t5-out.txt'
    results_file='6-t5/results/'
    file_path=os.path.join(results_file,'sys-file.txt')
    if not os.path.exists(results_file):
        os.makedirs(results_file)
    if not os.path.exists(file_path):
        os.system(r"touch {}".format(file_path))  # 调用系统命令行来创建文件
    sys.stdout = open(file_path, "w")   #os.path.join('aaaa','./bbb','sys-file.txt')

    retr_sents(query, corpus)
##用法：修改路径名称，点击运行。
