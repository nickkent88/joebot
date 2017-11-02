import os

from joebot import JoeBot

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
BOT_ID = os.environ.get("BOT_ID")

joe = JoeBot('starterbot', SLACK_BOT_TOKEN, BOT_ID)
joe.wake()