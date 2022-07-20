Environment.yml
'也可以使用 -export 选项生成一个 environment.yml 文件，以在 不同的平台和操作系统之间 复现项目环境。 
spec list 文件和 environment.yml 文件之间的区别在于： 
environment.yml 文件不针对特定操作系统，并且使用YAML格式。
environment.yml 仅列出了软件包名称，由 conda 基于软件包的名称构建环境。 

另一个区别是 -export 还包括使用pip安装的软件包，而 spec list 则没有。

 # '导出 environment.yml 文件：
!conda env export > py36-gram2.yml
#'注意：如果当前路径已经有了 environment.yml 文件，conda 会重写这个文件

#重现环境：
conda env create -f grammer_check/py36-gram2.yml
Conda 环境迁移.py
