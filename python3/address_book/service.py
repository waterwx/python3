# coding=UTF-8
import dao

__version__='1.0'

menumain = '''
******我的地址簿******

    1-浏览
    2-新建
    3-编辑
    4-删除

----------------------
'''
title=['序号','姓名','年龄','邮箱','电话']
class AddressService:
    '''地址簿服务层'''
    def __init__(self):
        '''程序加载时读取数据库现有的地址簿'''
        self.add = dao.AddressDao()
        self.add.readaddressMap()

    def showMainMenu(self):
        '''展示主菜单'''
        print(menumain)

    def inputCode(self):
        '''接收用户输入指令'''      
        try:
            code = input('请选择需要进行的操作:')
        except EOFError:
            print('谢谢使用,再见')
        except KeyboardInterrupt:
            print('谢谢使用,再见')
        else:
            if code=='1':
                self.readAddress()
            elif code=='2':
                self.newAddress()
            elif code=='3':
                self.editAddress()
            elif code=='4':
                self.delAddress()
            self.inputCode()

    def readAddress(self):
        '''浏览功能'''
        print('\n浏览\n')
        print('\t\t'.join(title))
        keys = list(self.add.addressMap.keys())
        keys.sort(key=lambda i:i)
        for key in keys:
            print('\t\t'.join(self.add.addressMap[key]).replace('\n',''))
        self.showMainMenu()

    def newAddress(self):
        '''新建功能'''
        print('\n新建\n')
        name = ""
        while name=="":
            name=input('请输入*姓名:')
        age = ""
        while age=="":
            age=input('请输入年龄:')
        mail = ""
        while mail=="":
            mail=input('请输入邮箱:')
        phone = ""
        while phone=="":
            phone=input('请输入电话')
        self.add.saveAddress(name,age,mail,phone)
        print('保存成功')
        self.showMainMenu()

    def editAddress(self):
        '''编辑功能'''
        print('\n编辑\n')
        willEdit = input('请输入想要编辑的序号:')
        if willEdit in self.add.addressMap:
            name = ""
            while name=="":
                name=input('请输入*姓名:')
            age = ""
            while age=="":
                age=input('请输入年龄:')
            mail = ""
            while mail=="":
                mail=input('请输入邮箱:')
            phone = ""
            while phone=="":
                phone=input('请输入电话:')
            self.add.updateAddress(willEdit,name,age,mail,phone)
            print('修改成功')           
        else:
            print('找不到要修改的序号')
        self.showMainMenu()

    def delAddress(self):
        '''删除功能'''
        print('\n删除\n')
        willDel = input('请输入想要删除的序号:')
        if willDel in self.add.addressMap:
            self.add.delAddress(willDel)
            print('删除成功')       
        else:
            print('找不到想要删除的序号')
        self.showMainMenu()
