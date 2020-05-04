# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import ssl
import requests
import os
import sys

def line(body):
    url = "https://notify-api.line.me/api/notify"
    access_token = 'I89UnoDRgRSInUXJOTg5fAniBE08CUuxVqj8ythMLt8'
    headers = {'Authorization': 'Bearer ' + access_token}
    message = body
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload,)


def send_image():
    url = "https://notify-api.line.me/api/notify"
    access_token = 'I89UnoDRgRSInUXJOTg5fAniBE08CUuxVqj8ythMLt8'
    # File Name
    FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")
    headers = {'Authorization': 'Bearer ' + access_token}
    message = 'この画面のエラーで落ちました'
    image = FILENAME
    payload = {'message': message}
    files = {'imageFile': open(image, 'rb')}
    r = requests.post(url, headers=headers, params=payload, files=files,)




#####################
###参考として##########
#sleniumでのスクショの撮り方
####################
# File Name
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")
# Get Screen Shot
chrome.save_screenshot(FILENAME)
# get width and height of the page
w = chrome.execute_script("return document.body.scrollWidth;")
h = chrome.execute_script("return document.body.scrollHeight;")
# set window size
chrome.set_window_size(w,h)
mail.send_image()