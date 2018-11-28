# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import sys
sys.path.append("\util")
from util import ObjectMap


class HomePage_baidu():

    def __init__(self,driver,congfile):
        self.__element = None
        self.__driver = driver
        self.__objectMap = ObjectMap.ObjectMap(congfile)


    def homePageLink(self):
        self.__element = self.__driver.find_element(by=str(self.__objectMap.getLocator("baidu","homePage")[0]),value=str(self.__objectMap.getLocator("baidu","homePage")[1]))
        return self.__element