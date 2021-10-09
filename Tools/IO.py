import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context


class GetDataFromUrl:

    __url__ = "https://algs4.cs.princeton.edu/"

    def __init__(self, url):
        self.url = url

    def downloaddata(self):
        with urllib.request.urlopen(self.url) as f:
            data = f.read().decode()
        path = self.url.replace(GetDataFromUrl.__url__, "../data/")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path,'w') as f:
            f.writelines(data)



test = GetDataFromUrl('https://algs4.cs.princeton.edu/11model/largeText.txt')
test.downloaddata()
