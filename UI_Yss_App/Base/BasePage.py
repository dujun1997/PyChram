# -*- coding: utf-8 -*- 
# @Time : 2020/12/11 10:37 
# @Author : dujun
# @describe : AppiumBase页面
# @File : BasePage.py
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    ##基础配置
    def __init__(self, desired_caps):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    # ID定位
    def By_ID(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_id(element), OverText)

    # Xpath定位
    def By_Xpath(self, element=None, OverText=None):
        return WebDriverWait(self.driver, 6, 0.5).until(lambda X: self.driver.find_element_by_xpath(element), OverText)

    def get_attribute(self, method=None, ele=None):
        location = self.driver.find_element(method, ele, )
        location.click()
        return location.get_attribute()
        ##clear()清除文本框数值

    def Clear(self):
        pass
