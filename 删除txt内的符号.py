def write_in_file(file_path,data):
    f = open(file_path, 'w')  # 若是'wb'就表示写二进制文件
    f.write(data)  # 写入一行
    f.close()


def read_file(file_path):
    f = open(file_path,encoding='utf8')
    line = f.readlines()
    return line

# ecoding=utf-8
ifn = "operators.txt"
ofn = "operators2.csv"

# outfile = open(ofn,'w') # 在使用write()函数的时候，如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错。
# result = read_file(ifn)
# print(result)
# result_all=[]
# # 使用正则表达式去匹配标点符号
# for i in range(len(result)):
#     result2 = result[i].replace('\n','')
#     result2 = result2.replace('"','')
#     print('result2',result2)
#     result_all = np.append(result_all, [result2], axis=0)  # 添加整行元素（每个小行），axis=1添加整列元素# result1 = demo(result)
# result_all = pd.DataFrame(result_all)
# with open(ofn, 'w') as w:
#     # result_all.to_csv(path_or_buf=ofn, header=False, index=False, sep=',')  # 设置分割符和括号内一样，后期py去掉双引号就可以直接分成多列。
#     result_all.to_csv(ofn, index=False, sep=',')
