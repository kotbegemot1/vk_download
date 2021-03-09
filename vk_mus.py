import vk_api
from vk_api import audio
import requests
from time import time
import os

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
path = '/home/kotbegemot/Документы/' + name_dir
login = 'kk1slorod@gmail.com'
password = 'proimbagosupers1ibhjvfcjdj1'
my_id = 'id20501806'

if not os.path.exists(path):
	os.makedirs(path)