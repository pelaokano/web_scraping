# -*- coding: utf-8 -*-
"""
Created on Mon May 24 15:09:55 2021

@author: adria
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path=r"C:\Users\adria\Documents\Trabajo_python\web_scraping\chromedriver.exe")

url="https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-del-sistema/"

meses=['0','1','2','3','4','5','6','7','8','9','10','11']
anos=['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
#anos=['2013']
#anos=['2013']

driver.get(url)

for a in anos:
    for m in meses:

        time.sleep(5)
        
        select1 = Select(driver.find_element_by_class_name('tipo-descarga'))
        select1.select_by_value('central')
        
        driver.find_elements_by_id('datepicker777-9761_2')[0].click()
                       
        select2 = Select(driver.find_element_by_class_name('ui-datepicker-month'))
        select2.select_by_value(m)
                      
        select3 = Select(driver.find_element_by_class_name('ui-datepicker-year'))
        select3.select_by_value(a)
                
        driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/button[2]').click()
                
        driver.find_element_by_xpath('//*[@id="Collapse2"]/div/article/div[2]/div/div/form/div/div[4]/a').click()
                        
        #driver.close()

