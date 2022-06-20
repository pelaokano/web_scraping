# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:09:12 2021

@author: adria
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path=r"C:\Users\adria\Documents\Trabajo_python\web_scraping\chromedriver.exe")

url="https://pgp.coordinador.cl/irequests"

driver.get(url)

time.sleep(5)

div_nombre=driver.find_element_by_xpath('//*[@id="filtroPorNombres"]/div[2]')

