# coding=utf-8  
import cPickle as p  
import os   
class Person:  
    def __init__(self, name, type, email, phone):  
        self.type = type  
        self.email = email  
        self.phone = phone  
        self.name = name  
    def changeType(self,type):  
        self.type = type  
    def changeName(self,name):  
        self.name = name  
    def changeEmail(self,email):  
        self.email = email  
    def changePhone(self,phone):  
        self.phone = phone  
addrlistfile = 'bat.data'  
if os.path.isfile(addrlistfile) == False:  
    f = open(addrlistfile,'w+')  
    f.close()  
while True:  
    f = open(addrlistfile,'rb+')  
    storeddict = {}  
    try:  
        storeddict = p.load(f)#每次都要进行重新载入  
    except EOFError:  
        print ('目前通讯薄为空！\n')  
    action = input('选择你的操作(输入数字键):\n\  
    1.添加\n\  
    2.修改\n\  
    3.删除\n\  
    4.搜索\n\  
    0.退出\n\')  
    if(action == 0):#退出  
        break  
    elif(action == 1):#添加  
        type = raw_input('输入用户类型（家人，朋友，等）:\n')  
        name = raw_input('输入用户名：\n')  
        if storeddict.has_key(name):  
            print r'用户名已存在！\n'  
            f.close()  
            continue  
        email = raw_input('输入用户email:\n')  
        phone = raw_input('输入用户电话:\n')  
        person = Person(name,type,email,phone)  
        storeddict[name]=person  
        p.dump(storeddict, f)  
        print ('添加成功\n')  
    elif(action == 2):#修改  
        name = raw_input('输入用户名：\n')  
        if (storeddict.has_key(name) != True):  
            print r'用户名不存在！\n'  
            f.close()  
            continue  
        person= storeddict[name]  
        del storeddict[name]  
        changetype = input('输入需要修改的值,1.type, 2.email, 3.phone\n')  
        if(changetype == 1):  
            type = raw_input('输入修改类型（家人，朋友，等）:\n')  
            person.changeType(type)  
        elif(changetype == 2):  
            email = raw_input('输入email:\n')  
            person.changeEmail(email)  
        elif(changetype == 3):  
            phone = raw_input('输入phone:\n')  
            person.changeEmail(phone)  
        else:  
            print ('修改值类型输入错误\n')  
        storeddict[name]=person  
        p.dump(storeddict, f)  
    elif(action == 3):#删除  
        name = raw_input('输入用户名：\n')  
        if storeddict.has_key(name) == False:  
            print r'用户名不存在！\n'  
            f.close()  
            continue  
        del storeddict[name]  
        p.dump(storeddict, f)  
    elif(action == 4):#搜索  
        name = raw_input('输入用户名：\n')  
        if storeddict.has_key(name) == False:  
            print r'用户名不存在！\n'  
            f.close()  
            continue  
        print storeddict[name].name,storeddict[name].type,storeddict[name].email,storeddict[name].phone  
    else:  
        print '选项不存在！\n'  
    f.close()  
print '谢谢使用!\n'
