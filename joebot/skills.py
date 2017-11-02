from .joebot import JoeBot


@JoeBot.handles('testing')
def testing(bot, event):
    return 'No, you\'re testing me.'

@JoeBot.handles('help')
def help(bot, event):
    pass

@JoeBot.handles('show')
def show(bot, event):
    pass

@JoeBot.handles('echo')
def echo(bot, event):
    message = event['text'].split(event['text'])[1].strip().lower()
    command = message.split()[0]
    content = message.lstrip(command)
    bot.post_message(content)

@JoeBot.handles('')
def no_retort(bot, event):
    pass