import os

print(os.getcwd())
from joebot import JoeBot
from joebot import skills

SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
BOT_ID = os.environ.get("BOT_ID")
HOME_CHANNEL = 'G5V408N76'
print(JoeBot.rules)


joe = JoeBot('starterbot', SLACK_BOT_TOKEN, BOT_ID)
joe.post_message(joe.name + ' reporting for duty!', HOME_CHANNEL)
joe.wake()