# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:14:33 2025

@author: Deepu
"""

import bs4
import requests

res = requests.get("http://127.0.0.1:3000/vcard-personal-portfolio-master/index.html")
soup = bs4.BeautifulSoup(res.text,'lxml')

#Access the Class Data.
soup.select('.contact-form')