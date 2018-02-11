import requests
from download_img import gen_naturals

naturals = gen_naturals()
url = 'http://users.skynet.be/fa046054/home/P22/track39.mp3'


def download_file(url, name=False):
    req = requests.get(url)

    filename = name if name else '{}.mp3'.format(next(naturals))

    file = open(filename, 'wb')
    file.write(req.content)
    file.close()


download_file(url, name='my_file.mp3')
