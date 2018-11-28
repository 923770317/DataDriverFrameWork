# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import sys
sys.path.append("\util")
from util import ObjectMap

class LoginPage():

    def __init__(self,driver,congfile):
        self.__element = None
        self.__driver = driver
        self.__objectMap = ObjectMap.ObjectMap(congfile)


    #返回页面中用户名输入框中的页面元素对象
    def userName(self):
        self.__element = self.__driver.find_element(self.__objectMap.getLocator("126mail","username"))
        return self.__element

    #返回页面中密码输入框中的页面元素对象
    def passWord(self):
        self.__element = self.__driver.find_element(self.__objectMap.getLocator("126mail","password"))
        return self.__element

    def loginButton(self):
        self.__element = self.__driver.find_element(self.__objectMap.getLocator("126mail","loginButton"))
        return self.__element

    def searchBox(self):
        self.__element = self.__driver.find_element(by=str(self.__objectMap.getLocator("baidu","mainPage")[0]),value=str(self.__objectMap.getLocator("baidu","mainPage")[1]))
        return self.__element