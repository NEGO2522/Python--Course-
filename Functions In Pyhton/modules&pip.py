'''
Two types of modules in pyhton:
- Enternal Modules (Installed using pip) 
- Built in Modules (Pre Installed Module In Python)
'''

# Build in modules for more built in modules u can visit this link:-  (https://docs.python.org/3/py-modindex.html)
import math
print(math.sqrt(16));

import random 
print(random.randint(1,100))

import datetime
print(datetime.datetime.now())

import os 
print(os.getcwd())

import statistics
print(statistics.mean({1,2,3})) 

import platform
print(platform.system())



import mymodule
mymodule.hello()


# # External Module 
# import requests
# r = requests.get("https://www.google.com")
# print(r.text)