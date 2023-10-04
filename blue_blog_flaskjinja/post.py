import requests


class Post:

    def get_blogs(self):
        url = "https://api.npoint.io/c790b4d5cab58020d391"
        contents = requests.get(url)
        return contents.json()