##  os.popen（）
具体用法如下：

result = os.popen('ipconfig')
#返回的结果是一个<class 'os._wrap_close'>对象，需要读取后才能处理

```css
context = result.read()
for line in context.splitlines():
    print(line)
result.close()

https://zhuanlan.zhihu.com/p/117495961
