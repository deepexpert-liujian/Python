
简单的‘Hello World!’

Python命令行
假设你已经安装好了Python, 那么在Linux命令行输入:

$python

将直接进入python。然后在命令行提示符>>>后面输入:

>>>print('Hello World!')

可以看到，随后在屏幕上输出:

Hello World!
print是一个常用函数，其功能就是输出括号中得字符串。

（在Python 2.x中，print还可以是一个关键字，可写成print 'Hello World!'，但这在3.x中行不通 ）
写一段小程序
另一个使用Python的方法，是写一个Python程序。用文本编辑器写一个.py结尾的文件，比如说hello.py
在hello.py中写入如下，并保存:
print('Hello World!')
退出文本编辑器，然后在命令行输入:

$python hello.py
来运行hello.py。可以看到Python随后输出
Hello World!

我们还可以把Python程序hello.py改成一个可执行的脚本，直接执行：
#!/usr/bin/env python
print('Hello World!')
需要修改上面程序的权限为可执行：
chmod 755 hello.py
然后再命令行中，输入
./hello.py
就可以直接运行了
