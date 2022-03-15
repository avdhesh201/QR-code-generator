# -*- coding: utf-8 -*-
"""qr generator.pynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18wJmtaoLgT5Qdg1Hhv5mLay-35jDRZB8
"""

# simplest Qr code generator using python modules
''' CREATED BY AVDHESH KUMAR SINGH '''

!pip install pyqrcode   #installation  of pyqrccode module

import pyqrcode  # importing the module
from pyqrcode import QRCode 
  
# String to QR code generator
github = "https://github.com/avdhesh201"
  
# Creation of QR
url = pyqrcode.create(github) 
  
# Creaed and saving the png file
url.svg("avdhesh.svg", scale = 8)