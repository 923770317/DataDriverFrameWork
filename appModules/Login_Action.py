# -*- coding: utf-8 -*-
import sys
sys.path.append("\pageObjects")
from pageObjects import LoginPage
from selenium import webdriver
import time

class Login_Action(object):

    @staticmethod
    def execute(driver,keyword):
        # driver.get("https://www.baidu.com")
        loginPage =LoginPage.LoginPage(driver,"..\confile.conf")
        loginPage.searchBox().send_keys(keyword)
        time.sleep(5)