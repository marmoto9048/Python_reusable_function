from gec_model import GecBERTModel
from predict_sent2 import grammer_use
from grammer_score import final_score
import argparse
def grammar_checker(input_sent):
    input_sent_list=['']*1
    input_sent_list[0]=input_sent
    output_sent=grammer_use(input_sent_list)
    str_sent_gram=str(output_sent[0])
    final_score_out=final_score(str_sent_gram)
    return str_sent_gram,final_score_out

if __name__=='__main__':
    import sys
    input_sentence=str(sys.argv[1])
    # print('得到的输入句子：',input_sentence)
    output_sent,final_score = grammar_checker(input_sentence)
    # print('sentence score:', output_sent,final_score)
    print( output_sent,final_score)

