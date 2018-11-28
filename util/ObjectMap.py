#coding=utf-8
import ConfigParser
from selenium.webdriver.common.by import By

class ObjectMap():

    #初始化 ObjectMap 类,读取配置文件
    def __init__(self,congFilePath):
        try:
            self.cp = ConfigParser.SafeConfigParser()
            self.cp.read(congFilePath)
        except Exception,e:
            print "读取配置文件失败" , e.message

    def getLocator(self,section,elementNmaeInpropFile):
        locator = self.cp.get(section,elementNmaeInpropFile)
        locatorType = str(locator).split("=")[0]
        locatorValue = str(locator).split("=")[1]
        # print locatorType,"----",locatorValue
        if locatorType.lower() == "id":
            return (By.ID,locatorValue)
        elif locatorType.lower() == "name":
            return (By.NAME,locatorValue)
        elif locatorType.lower() == "classname" or locatorType.lower() == "class":
            return (By.CLASS_NAME,locatorValue)
        elif locatorType.lower() == "tagname" or locatorType.lower() == "tag":
            return (By.TAG_NAME,locatorValue)
        elif locatorType.lower() == "linktext" or locatorType.lower() =="link":
            return (By.LINK_TEXT,locatorValue)
        elif locatorType.lower() =="partiallinktext":
            return (By.PARTIAL_LINK_TEXT,locatorValue)
        elif locatorType.lower() == "cssselector" or locatorType.lower() =="css":
            return (By.CSS_SELECTOR)
        elif locatorType.lower() == "xpath":
            return (By.XPATH,locatorValue)
        else:
            raise Exception("输入的locatorType在配置文件中没有别定义",locatorType)


if __name__ =="__main__":
    obj = ObjectMap("..\confile.conf")
    obj.getLocator("hahah","xixix")

