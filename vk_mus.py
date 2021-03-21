import vk_api
from vk_api import audio
import requests
from time import time
import os
import info

REQUEST_STATUS_CODE = 200
name_dir = 'music_vk'
path = info.path_mus + name_dir
login = info.login
password = info.password
my_id = info.my_id

print(login, password, my_id, sep='')

if not os.path.exists(path):
	os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)

os.chdir(path)

qwe = vk_audio.search("nice", 10, 0)

r = next(qwe)

req = requests.get(r["url"])

with open(r["artist"] + '_' + r["title"] + '.mp3', 'wb') as output_file:
	output_file.write(req.content)