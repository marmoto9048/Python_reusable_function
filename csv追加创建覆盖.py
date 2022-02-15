#创建  利用csv包中的writer函数，如果文件不存在，会自动创建，需要注意的是，文件后缀一定要是.csv，这样才会创建csv文件
#这里创建好文件，将csv文件的头信息写进了文件。
import csv
def create_csv():
    path = "aa.csv"
    with open(path,'wb') as f:
        csv_write = csv.writer(f)
        csv_head = ["good","bad"]
        csv_write.writerow(csv_head)
 
#追加
def write_csv():
    path  = "aa.csv"
    with open(path,'a+') as f:
        csv_write = csv.writer(f)
        data_row = ["1","2"]
        csv_write.writerow(data_row)


# 覆盖

#读取：
#利用csv.reader可以读csv文件，然后返回一个可迭代的对象csv_read，我们可以直接从csv_read中取数据
def read_csv():
    path = "aa.csv"
    with open(path,"rb") as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            print line
            
# 在用pandas输出csv时，如果不对第一行和第一列进行定义，pandas会自动用数字序号补齐，但有时候我们只想单纯输出数据，不想要表头或者序号，那么就需要以下的操作：
output = pd.DataFrame(data=list1)
output.to_csv('save_path', header=None, index=None)
