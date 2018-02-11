import requests
import urllib.request


def gen_naturals():
    i = 0
    while True:
        yield i
        i += 1


naturals = gen_naturals()


def download_image(url, original_name=False):
    name = next(naturals)
    full_name = '{}.jpg'.format(name)

    if original_name:
        full_name = url.split('/')[-1]

    urllib.request.urlretrieve(url, full_name)


if __name__ == '__main__':
    url = 'https://3.bp.blogspot.com/-QXusbOoSAVs/VHELiPp5RQI/AAAAAAAAD9A/8RBwkpLfLDY/s1600/python.png'
    download_image(url, original_name=True)
