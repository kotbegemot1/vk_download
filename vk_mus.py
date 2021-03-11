import vk_api
from vk_api import audio
import requests
from time import time
import os

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
path = '/home/kotbegemot/Документы/' + name_dir
login = ''
password = ''
my_id = ''

if not os.path.exists(path):
	os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)