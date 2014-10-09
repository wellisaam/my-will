from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings

from helpers.gif_scott_heron import GifMeUpScotty

class GifPlugin(WillPlugin):

    def __init__(self, *args, **kwargs):
        self.giffy = GifMeUpScotty()
        return WillPlugin.__init__(self, *args, **kwargs)

    @respond_to("^gif me (?P<search_query>.*)$")
    def define(self, message, search_query):
        """gif me ___ : Search google images for ___, and post a random one."""
        return self.reply(message, self.giffy.get_me(search_query))
