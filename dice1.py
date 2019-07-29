# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests


url = 'https://www.dice.com/jobs?l=FL&sort=date&p=2' 
headers = {'user-agent': 'my-app-test/0.0.1'}
r = requests.get(url, headers=headers)
print (r.text)