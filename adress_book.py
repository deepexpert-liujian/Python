-- coding: UTF-8 --
#实现简单通讯录系统
import os
import pickle
#判断通讯录是否存在，不存在创建的
if os.path.exists(r'D:\person.txt') == False:
f = open('D:\person.txt', 'w')
temp = {'total': 0}
pickle.dump(temp, f)
f.close()
else:
pass

#添加联系人
def add():
f = open('D:\person.txt', 'r')
A = pickle.load(f)
f.close()
count = 0
name = raw_input('请输入要添加的联系人的姓名：')
for key in A.keys():
count += 1
if key == name and count <= A['tatal'] + 1:
print '添加失败，改联系人已存在'
break
if count == A['tatal'] + 1 and key != name:
number = raw_input('请输入号码:')
member = {name:number}
A['tatal'] += 1
A.update(member)
f = open('D:\person.txt', 'w')
pickle.dump(A, f)
f.close()
print 'Success!'
break

#删除
def delete(name):
f = open('D:\Person.txt', 'r')
A = pickle.load(f)
f.close()
count = 0
for key in A.keys():
count += 1
if key == name and count <= A['total'] + 1:
A.pop(name)
A['total'] -= 1
f = open('d:\Person.txt', 'w')
pickle.dump(A, f)
f.close()
print("删除成功!")
break
if count == A['total'] + 1 and key != name:
print("联系人不存在！无法删除！")
break
#显示所有联系人
def show_all():
f = open('d:\person.txt', 'r')
A = pickle.load(f)
print("一共有{}个联系人.".format(A['total']))
for key in A.keys():
if key != 'total':
print("{""}:{""}".format(key, A[key]))
f.close()
#查找
def search(name):
f = open('D:\person.txt', 'r')
A = pickle.load(f)
count = 0
for key in A.keys():
count += 1
if key == name and count <= A['total']+1:
print("{}的号码是: {}".format(name, A[key]))
break
if count == A['total']+1 and key != name:
print("联系人不存在!")
break
f.close()

#修改
def change():
x = input("请输入所要修改联系人姓名:")
f = open('d:\person.txt', 'r')
A = pickle.load(f)
f.close()
count = 0
for key in A.keys():
count += 1
if key==x and count <= A['total']+1:
y = input("请输入修后的号码:")
A[key] = y
f=open('d:\person.txt', 'w')
pickle.dump(A, f)
f.close()
print "修改成功!"
break
if count == A['total']+1 and key != name:
print "联系人不存在！"
break

#退出通讯录
def exit():
exec "quit()"
#界面
def instructions():
print ("----------------------------------")
print ("显示提示信息: *")
print ("显示所有联系人:0")
print ("查找联系人: 1")
print ("添加联系人: 2")
print ("删除联系人: 3")
print ("更改联系人资料:4")
print ("退出通讯录: 5")
print ("----------------------------------")

#主程序
instructions()
while True:
x = raw_input("请输入您的选择:")
if x == '2':
add()
continue
if x == '0':
show_all()
continue
if x == '5':
exit()
continue
if x == '1':
name = raw_input("请输入所要查找联系人的姓名:")
search(name)
continue
if x == '3':
name = raw_input("请输入所要删除联系人的姓名:")
delete(name)
continue
if x == '4':
change()
continue
if x == '*':
instructions()
else:
print("输入选项不存在，请重新输入！")
continue