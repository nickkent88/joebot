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
        
    def listen(self):
        read_period = 1 # read websocket every 1 second
        if slack_client.rtm_connect():
            while True:
                command, channel = parse_slack_output(slack_client.rtm_read())
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
        output_list = slack_client.rtm_read()
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(AT_BOT)[1].strip().lower(), \
                        output['channel']
        return None, None

    def start_message(self):
        print("Nudging JoeBot awake.")
        time.sleep(1)
        print("...")
        time.sleept(1)
        print("Ideology!")
        

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


