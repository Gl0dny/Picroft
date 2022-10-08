from adapt.intent import IntentBuilder
from mycroft import Mycroftskill, intent_handler
from mycroft.util.log import LOG

import requests

class MyRobot(Mycroftskill):
    def __init__(self):
        super().__init__()
        self.base_url = self.settings.get("base_url")

def handle_control(self, end_point, dialog_verb):
    try:
        requests.post(self.base_url + end_point)
        #searching for dialogs which are to be outputed
        self.speak_dialog('Robot')
        self.speak_dialog(dialog_verb)
    except:
        self.speak_dialog("UnableToReach")
        #print to mycroft console
        LOG.exception("There was an error connecting to the robot")

def create_skill():
    return MyRobot()

#searching for words
@intent_handler(IntentBuilder("")   
                .require("Robot")
                .require("TestRainbow"))
def handle_test_rainbow(self, message):
    self.handle_control("/run/test_rainbow", "TestingRainbow")   

@intent_handler(IntentBuilder("")
                .require("Robot")
                .require("stop"))
def handle_stop(self, message):
    self.handle_control("/stop", "stopping")


