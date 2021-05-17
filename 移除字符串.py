test_str = "aaaa\nAcknowledgments We thank the anonymous The cross-lingual links are used to link the longer-lasting stories across languages.<\START><END>The"
# test_str = "The cross-lingual links are used to link the "

# print("原始字符串为 : " + test_str)# 输出原始字符串
new_str = ""
a=test_str.find('<\START>')# 移除<\START>字符
# b=test_str.find('\n')# 移除\n字符
# print('有没有找到：',a)
if a ==-1:
    new_str2= test_str.replace('\n', '').replace('\r', '')
else:
    for i in range(0, len(test_str)):
        if i < a :
            new_str = new_str + test_str[i]
            new_str2=new_str.replace('\n', '').replace('\r', '')
print("字符串移除后为 : " + new_str2)