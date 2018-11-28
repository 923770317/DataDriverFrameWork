 #-*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
import ddt
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("\pageObjects")
sys.path.append("\appModules")
sys.path.append("\util")
from pageObjects import LoginPage
from appModules import Login_Action
from util import ExcelUtil
from util import Constant
from util import Log

ExcelUtil.ExcelUtil.setExcelFile(Constant.Constant.TestDataExcelFilePath,Constant.Constant.TestDataExcelFileSheet)

@ddt.ddt
class TestMail126Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.baseUrl = Constant.Constant.Url


    def tearDown(self):
        self.driver.quit()

    @ddt.data(*ExcelUtil.ExcelUtil.getValue())
    @ddt.unpack
    def test_MailLoginDemo1(self,testCaseName,keyWord,result,isExecute):
        if isExecute == "y":
            driver = self.driver
            driver.get(self.baseUrl)
            print "开始了",testCaseName

            Login_Action.Login_Action.execute(driver,keyWord)

            time.sleep(5)
            #增加个断言的地方
            ExcelUtil.ExcelUtil.setCellData(1,2,"succ",Constant.Constant.TestDataExcelFilePath)


if __name__ =="__main__":
    unittest.main()