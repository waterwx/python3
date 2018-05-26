# coding=UTF-8
#数据层

#数据库文件
datafile='address.data'
#连接符
contact=',,,'

__version__='1.0'

class AddressDao:
    '''地址簿数据层'''
    def __init__(self):
        self.addressMap={}
        self.number = '0'
    def readaddressMap(self):
        '''读取地址簿所有内容'''
        with open(datafile) as f:
            for line in f:
                address = line.split(contact)
                self.addressMap[address[0]]=address
                self.number=address[0]

    def saveAddress(self,name,age,mail,phone):
        '''保存一条记录'''
        newSeq = str(int(self.number)+1)
        addressNew = [newSeq,name,age,mail,phone]
        self.addressMap[newSeq]=addressNew
        self.saveAddressToFile()

    def saveAddressToFile(self):
        '''持久化到文件'''
        with open(datafile,'w') as f:
            keys = list(self.addressMap.keys())
            keys.sort(key=lambda i:i)
            for key in keys:
                f.writelines(contact.join(self.addressMap[key]))

    def updateAddress(self,code,name,age,mail,phone):
        '''修改一条记录'''
        addressNew = [code,name,age,mail,phone]
        self.addressMap[code]=addressNew
        self.saveAddressToFile()

    def delAddress(self,code):
        '''删除一条记录'''
        del(self.addressMap[code])
        self.saveAddressToFile()
