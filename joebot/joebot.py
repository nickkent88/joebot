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
        self.at_str = "<@" + bot_id + ">"
        
    def wake(self):
        read_period = 1 # read websocket every 1 second
        if self.client.rtm_connect():
            self._start_message()
            while True:
                event = self._parse_stream()
                if event:
                    self._handle_event(event)
                time.sleep(read_period)
        else:
            raise RuntimeError("Connection unsuccessful. Check Slack token and ID.")

    def _handle_event(self, event):
        handler = self._dispatch_handler(event)
        handler(event)

    def _handle_command(self, event):
        message = event['text'].split(self.at_str)[1].strip().lower()
        command = message.split()[0]
        if command in JoeBot.rules:
            return JoeBot.rules[command](event)
        else:
            return "Sorry, I don't understand that command."

    def _handle_message(self, event):
        for word in event['text'].split():
            if word in JoeBot.rules.keys():
                return JoeBot.rules[word]
            else:
                return JoeBot.rules[''] # return no-retort handler 

    def _handle_typing(self, event):
        pass

    def _handle_message_changed(self, event):
        pass

    def _handle_presence_change(self, event):
        pass

    def _not_implemented_handler(self, event):
        pass

    def _dispatch_handler(self, event):
        handlers = {
            'message': self._handle_message,
            'user_typing': self._handle_typing,
            'message_changed': self._handle_message_changed
            'presence_change': self._handle_presence_change
        }
        if event['type'] in handlers:
            return handlers[event['type']]
        else:
            return self._not_implemented_handler
            
    def _parse_stream(self):
        output_list = self.client.rtm_read()
        if output_list:
            for output in output_list:
                if (output and 'text' in output) and (self.at_str in output['text']):
                    # return text after the @ mention, whitespace removed
                    return output
        return None

    def _parse_stream_old(self):
        output_list = self.client.rtm_read()
        if output_list:
            for output in output_list:
                if (output and 'text' in output) and (self.at_str in output['text']):
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(self.at_str)[1].strip().lower(), \
                           output['channel']
        return None, None

    def _start_message(self):
        print("Nudging JoeBot awake...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("Ideology! (JoeBot is awake and listening)")
        
    def _post_message(self, message, channel):
        self.client.api_call("chat.postMessage", channel=channel, text=message, as_user=True)

    def get_users(self):
        api_call = self.client.api_call("users.list")
        if api_call.get('ok'):
            return api_call.get('members')
        else:
            return []

    def get_channels(self):
        pass
