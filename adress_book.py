-- coding: UTF-8 --
#ʵ�ּ�ͨѶ¼ϵͳ
import os
import pickle
#�ж�ͨѶ¼�Ƿ���ڣ������ڴ�����
if os.path.exists(r'D:\person.txt') == False:
f = open('D:\person.txt', 'w')
temp = {'total': 0}
pickle.dump(temp, f)
f.close()
else:
pass

#�����ϵ��
def add():
f = open('D:\person.txt', 'r')
A = pickle.load(f)
f.close()
count = 0
name = raw_input('������Ҫ��ӵ���ϵ�˵�������')
for key in A.keys():
count += 1
if key == name and count <= A['tatal'] + 1:
print '���ʧ�ܣ�����ϵ���Ѵ���'
break
if count == A['tatal'] + 1 and key != name:
number = raw_input('���������:')
member = {name:number}
A['tatal'] += 1
A.update(member)
f = open('D:\person.txt', 'w')
pickle.dump(A, f)
f.close()
print 'Success!'
break

#ɾ��
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
print("ɾ���ɹ�!")
break
if count == A['total'] + 1 and key != name:
print("��ϵ�˲����ڣ��޷�ɾ����")
break
#��ʾ������ϵ��
def show_all():
f = open('d:\person.txt', 'r')
A = pickle.load(f)
print("һ����{}����ϵ��.".format(A['total']))
for key in A.keys():
if key != 'total':
print("{""}:{""}".format(key, A[key]))
f.close()
#����
def search(name):
f = open('D:\person.txt', 'r')
A = pickle.load(f)
count = 0
for key in A.keys():
count += 1
if key == name and count <= A['total']+1:
print("{}�ĺ�����: {}".format(name, A[key]))
break
if count == A['total']+1 and key != name:
print("��ϵ�˲�����!")
break
f.close()

#�޸�
def change():
x = input("��������Ҫ�޸���ϵ������:")
f = open('d:\person.txt', 'r')
A = pickle.load(f)
f.close()
count = 0
for key in A.keys():
count += 1
if key==x and count <= A['total']+1:
y = input("�������޺�ĺ���:")
A[key] = y
f=open('d:\person.txt', 'w')
pickle.dump(A, f)
f.close()
print "�޸ĳɹ�!"
break
if count == A['total']+1 and key != name:
print "��ϵ�˲����ڣ�"
break

#�˳�ͨѶ¼
def exit():
exec "quit()"
#����
def instructions():
print ("----------------------------------")
print ("��ʾ��ʾ��Ϣ: *")
print ("��ʾ������ϵ��:0")
print ("������ϵ��: 1")
print ("�����ϵ��: 2")
print ("ɾ����ϵ��: 3")
print ("������ϵ������:4")
print ("�˳�ͨѶ¼: 5")
print ("----------------------------------")

#������
instructions()
while True:
x = raw_input("����������ѡ��:")
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
name = raw_input("��������Ҫ������ϵ�˵�����:")
search(name)
continue
if x == '3':
name = raw_input("��������Ҫɾ����ϵ�˵�����:")
delete(name)
continue
if x == '4':
change()
continue
if x == '*':
instructions()
else:
print("����ѡ����ڣ����������룡")
continue