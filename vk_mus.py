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

# print(login, password, my_id, sep='')

if not os.path.exists(path):
	os.makedirs(path)

vk_session = vk_api.VkApi(login=login, password=password)
vk_session.auth()
vk = vk_session.get_api()  # Теперь можно обращаться к методам API как к обычным 
                                        # классам
vk_audio = audio.VkAudio(vk_session)

os.chdir(path)

question = input("Введите название песни: ")

tracklist = []
for track in enumerate(vk_audio.search(question, 3, 0), 1):
	tracklist.append(track)
	print("{}. {} - {}".format(track[0], track[1]['artist'], track[1]['title']))

number_of_track = input("Введите порядковый номер песни которую хотите скачать: ")

for artist in tracklist:
	if artist[0] == int(number_of_track):
		req = requests.get(artist[1]["url"])
		with open(artist[1]["artist"] + '_' + artist[1]["title"] + '.mp3', 'wb') as output_file:
			output_file.write(req.content)
			print('downloaded')
		break
	else:
		print('not downloaded')
		continue

if __name__ == '__main__':
	pass


# qwe = vk_audio.search(str(question), 10, 0)

# r = next(qwe)

# req = requests.get(r["url"])

# with open(r["artist"] + '_' + r["title"] + '.mp3', 'wb') as output_file:
# 	output_file.write(req.content)

# tracklist = []
# for track in enumerate(vk_audio.search('love', 2, 0), 1):
# 	tracklist.append(track)
# 	print("{}. {} - {}".format(track[0], track[1]['artist'], track[1]['title']))

# for artist in tracklist:
# 	if artist[0] == 1:
# 		req = requests.get(artist[1]["url"])
# 		with open(artist[1]["artist"] + '_' + artist[1]["title"] + '.mp3', 'wb') as output_file:
# 			output_file.write(req.content)