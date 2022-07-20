# 假设英文句子为t
t ='After updating from 2.0.40 to 2.0.42, all POST-request to the cgi-bin are \
    broken, and return the script source-code! Request to the same scripts \
    function normal.\
    This is not a config issue, worked up to 2.0.40, and works for GET in 2.0.42'
def save(file,data):
    filename = open(file,'a+')
    for value in data:
        filename.write(str(value)+'\n')
    filename.close()
    print('saved in ',file)

def vocabulary_stat(file_name):
    with open(file_name, encoding='utf8') as file_obj:
        contents = file_obj.read()
    len_alcarc_vocabulary=len(set(contents.split()))# 去掉重复单词的句子长度 set()可去除重复值
    alcarc_vocabulary=set(contents.split())
    print('单词表长度：',len_alcarc_vocabulary)
    len_alcarc=len(contents.split())# 通过split划分英文句子中的单词  t.split()是list形式，采用len()方法计算长度
    print('出现过多少个单词',len_alcarc)
    # print('有多少个字符',len(contents))
    return alcarc_vocabulary  #返回单词表
#-0-------------------------------------------------------------------------------------------------------

file_name = './data/all.txt'
out_file_name = './data/train_vocab.txt'
alcarc_vocabulary=vocabulary_stat(file_name)
# test_source.txt  test_target.txt  train_source

save(out_file_name,alcarc_vocabulary)
print('已保存')

# 单词表长度： 538531
# 出现过多少个单词 29295953
# 有多少句 180116974
# saved in  ./data/train_vocab.txt
# 已保存
# 针对语料库中单词数量的统计

