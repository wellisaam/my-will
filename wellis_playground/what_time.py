import time
from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings


class HearTimePlugin(WillPlugin):

    @hear("the time", include_me=False)
    def will_speaking_clock(self, message):
        timenow = str(time.now())
        self.say(rendered_template("the time is now" + timenow, {}), message=message, html=True, )
