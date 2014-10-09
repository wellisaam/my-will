import requests
import random

class GifMeUpScotty(object):

    def gif_me(self, search_query):
        """gif me ___ : Search google images for ___, and post a random one."""
        data = {
            "q": search_query + "gif",
            "v": "1.0",
            "safe": "active",
            "rsz": "8"
        }
        r = requests.get("http://ajax.googleapis.com/ajax/services/search/images", params=data)
        try:
            results = r.json()["responseData"]["results"]
        except TypeError:
            results = []
        if len(results) > 0:
            url = random.choice(results)["unescapedUrl"]
            return ("%s" % url)
        else:
            return ("Couldn't find any gif!")

if __name__ == '__main__':
    gm = GifMeUpScotty()
    print gm.gif_me('gif me nic cage')
    print gm.gif_me('asdfasdf')
