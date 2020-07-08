import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ ファイルから画像を取得する """

    def __init__(self, path):
        self._path = path

    def get_image(self):
        return open(self._path, 'rb')


class RemoteImage:
    """ URLから画像を取得する """

    def __init__(self, url):
        self._url = url

    def get_image(self):
        data = requests.get(self._url)
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """ キーワード検索で画像を取得する """

    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HIGHT = 600

    def __init__(self, url):
        super().__init__(self.build_url(url))

    def build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HIGHT}/{keyword}')


KeywordImage = _LoremFlickr


def ImageSource(keyword):
    """ 最適なイメージソースを返す """
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    return ImageSource(keyword).get_image()
