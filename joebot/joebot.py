import os
import time

from functools import wraps
from slackclient import SlackClient


class JoeBot(object):
    rules = {}

    @classmethod
    def handles(cls, *keywords, **options):
        def decorator(func):
            for word in keywords:
                cls.add_rule(word, func, **options)
            return func
        return decorator

    @classmethod
    def add_rule(cls, word, callback):
        cls.rules[word] = callback

    def __init__(self, name, api_token, bot_id):
        self.name = name
        self.api_token = api_token
        self.bot_id = bot_id
        self.client = SlackClient(api_token)
        
    def wake(self):
        read_period = 1 # read websocket every 1 second
        if self.client.rtm_connect():
            self.start_message()
            while True:
                command, channel = self.parse_stream()
                if command and channel:
                    handle_command(command, channel)
                time.sleep(read_period)
        else:
            raise RuntimeError("Connection unsuccessful. Check Slack token and ID.")

    def handler(self, message):
        for word in message.split():
            if word in rules.keys():
                return rules[word]
            else:
                return rules[''] # return no-retort handler 
            
    def parse_stream(self):
        output_list = self.client.rtm_read()
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(AT_BOT)[1].strip().lower(), \
                        output['channel']
        return None, None

    def start_message(self):
        print("Nudging JoeBot awake...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Ideology! (JoeBot is awake and listening)")
        

    # slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


